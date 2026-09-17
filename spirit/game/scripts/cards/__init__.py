import os
import importlib.util
import logging
import sys
from typing import Any, Dict, List
from spirit.game.models.card import Card, PokemonCard
from spirit.game.attributes import AttrID, CardType

class ScriptLoader:
    """Dynamically loads card definition scripts from the filesystem."""
    def __init__(self, scripts_dir: str):
        self.scripts_dir = os.path.abspath(scripts_dir)
        self.cards: List[Card] = []
        self.cards_by_guid: Dict[str, Card] = {}
        self.cards_by_key: Dict[str, Card] = {}
        # script filename stem (e.g. "Watchog_79") -> archetype GUID
        self.cards_by_stem: Dict[str, str] = {}
        # scripts-relative reference ("HGSS1/LugiaLEGEND") -> definition, for
        # every script that loaded, published or not (LEGEND halves name
        # their combined Pokemon this way).
        self.definitions: Dict[str, Any] = {}
        self.last_errors: List[str] = []

    def load_all(self, force=False):
        """Loads all card scripts once; cached thereafter unless force=True.

        Re-running scripts rebuilds effect registries (ABILITIES_BY_ID etc.)
        and blocks the event loop ~1s, so hot paths must hit the cache.
        """
        if self.cards and not force:
            return self.cards
        self.cards = []
        self.cards_by_guid = {}
        self.cards_by_key = {}
        self.cards_by_stem = {}
        self.definitions = {}
        self.last_errors = []

        logging.info(f"[Scripts] Loading card scripts from {self.scripts_dir}...")

        # Two passes: every script runs first, then the LEGEND halves are
        # bound to their combined definition, and only then are the cards
        # published -- a half whose pair is missing or broken is left out,
        # and a combined (runtime-only) definition is never a card.
        loaded = []
        for root, _, files in os.walk(self.scripts_dir):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    file_path = os.path.join(root, file)
                    card_def = self._load_script(file_path)
                    if card_def is not None:
                        loaded.append((file_path, card_def))
        invalid = self._resolve_legends()
        for file_path, card_def in loaded:
            reference = self._reference(file_path)
            if reference in invalid or getattr(card_def, "runtime_only", False):
                continue
            try:
                self._publish(file_path, card_def)
            except Exception as e:
                self.last_errors.append(f"{reference}: {e}")
                logging.error(f"[Scripts] Failed to publish card {reference}: {e}")

        logging.info(f"[Scripts] Successfully loaded {len(self.cards)} card scripts.")
        return self.cards

    def _reference(self, file_path: str) -> str:
        rel = os.path.relpath(file_path, self.scripts_dir)
        return os.path.splitext(rel)[0].replace(os.path.sep, "/")

    def _resolve_legends(self):
        """Bind each LEGEND half to its combined definition; a pair must be
        one top and one bottom with distinct GUIDs, else both stay out."""
        invalid = set()
        pairs: Dict[str, list] = {}
        for reference, definition in self.definitions.items():
            if not hasattr(definition, "resolve_legend"):
                continue
            try:
                if definition.legend not in self.definitions:
                    raise ValueError(f"Missing LEGEND definition: {definition.legend}")
                definition.resolve_legend(self.definitions[definition.legend])
                pairs.setdefault(definition.legend, []).append((reference, definition))
            except (ValueError, TypeError) as error:
                invalid.add(reference)
                self.last_errors.append(f"{reference}: {error}")
                logging.error(f"[Scripts] LEGEND half {reference}: {error}")
        for reference, halves in pairs.items():
            problem = None
            if {half.half for _, half in halves} != {"top", "bottom"}:
                problem = "LEGEND requires both top and bottom printings"
            elif len({half.guid.lower() for _, half in halves}) != len(halves):
                problem = "LEGEND printings must have distinct GUIDs"
            if problem:
                for path, half in halves:
                    half.legend_definition = None
                    invalid.add(path)
                self.last_errors.append(f"{reference}: {problem}")
                logging.error(f"[Scripts] LEGEND {reference}: {problem}")
        return invalid

    def _load_script(self, file_path: str):
        """Runs a single card script and records its definition; returns the
        definition (None when the script has none or failed)."""
        try:
            # Create a unique module name based on the relative path
            rel_path = os.path.relpath(file_path, self.scripts_dir)
            module_name = "card_script_" + rel_path.replace(os.path.sep, "_").replace(".py", "")

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                logging.error(f"[Scripts] Could not create spec or loader for {file_path}")
                return None

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'card'):
                card_def = module.card
                self.definitions[self._reference(file_path)] = card_def
                return card_def
            logging.warning(f"[Scripts] Script {file_path} does not define a 'card' object.")
        except Exception as e:
            logging.error(f"[Scripts] Failed to load script {file_path}: {e}")
        return None

    def _publish(self, file_path: str, card_def):
        """Converts the Definition object into a Server Card model (what the
        packet handlers, collections and decks see)."""
        archetype = card_def.to_archetype_dict()
        guid = archetype["guid"]
        key = archetype["key"]
        attrs = archetype["attributes"]

        c_type = attrs.get(str(AttrID.CARD_TYPE.value), {}).get("value", CardType.UNSET)

        display_name = archetype.get("display_name")
        searchable_by = archetype.get("searchable_by", [])
        subtypes = getattr(card_def, "subtypes", [])

        if c_type == CardType.POKEMON:
            card_obj = PokemonCard(guid, key, attrs, display_name, searchable_by, subtypes)
        else:
            card_obj = Card(guid, key, attrs, display_name, searchable_by, subtypes)

        self.cards.append(card_obj)
        self.cards_by_guid[guid] = card_obj
        self.cards_by_key[key] = card_obj
        self.cards_by_stem[os.path.splitext(os.path.basename(file_path))[0]] = guid

# Global loader instance
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__))
loader = ScriptLoader(SCRIPTS_DIR)
