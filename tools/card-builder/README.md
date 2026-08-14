# Spirit Card Builder (local)

Local-only UI for scaffolding Spirit PTCGO Python card scripts using existing factories and similar card scripts from the codebase.

## Run

```bash
cd tools/card-builder
npm install
npm run sync-data              # once (or when you want catalog updates)
npm run generate:implemented-ids
npm run dev
```

Opens at [http://localhost:5174](http://localhost:5174).

## Browse cards (no live API)

Catalog data comes from a local clone of [PokemonTCG/pokemon-tcg-data](https://github.com/PokemonTCG/pokemon-tcg-data):

1. `npm run sync-data` shallow-clones/updates into `data/pokemon-tcg-data`
2. Vite serves that folder at `/tcg-data/*`
3. Browse series → set → card (or search by name) to pre-fill the generator

Reference art uses the `images.pokemontcg.io` URLs already in that JSON. On **Save**, the large image is downloaded to `spirit/assets/cards/<SET>/<Stem>_<number>.png`.

Implemented cards (from `implementedCardIds.json`) are greyed out in the card grid. Regenerate after adding scripts:

```bash
npm run generate:implemented-ids
```

## Generation rules

- Attack, Ability, and Trainer effect text uses a matching Spirit factory prefab when available (`draw_attack`, `condition_attack`, `flip_damage`, `snipe_attack`, `heal_item`, `search_to_hand`, `professors_research`, …).
- If no prefab matches, the builder searches existing scripts under `spirit/game/scripts/cards/**` for a strong same-kind `game_text` match and reuses that `effect=` expression (plus helpers/imports when possible). Copied helper functions are renamed to the new attack, ability, or card title (`Leaf Guard` / `leaf_guard` → `Protect Charge` / `protect_charge`), and helper docstrings are updated to this card's damage and text.
- Trainer cards also split effect text into clauses, match each clause against factories and other trainers, and stitch those pieces into one named helper when needed. Shared trainer factories in `spirit/game/card_effects/trainers.py` (Ultra Ball, Professor's Research, Switch, …) are part of that corpus.
- If a trainer (or other card) has the **exact same display name** as an already-implemented script in any set/format, the builder offers a `reprint()` stub. Trainers auto-select reprint; the source may live in another set folder (`sibling_card(__file__, "../SWSH9/UltraBall_150.py")` plus `set_code=` / `key=`).
- If neither a prefab nor a sufficiently similar script is found, text is preserved with `effect=unimplemented`.
- Empty attack text (damage-only) emits no `effect`.
- Output is a Python `*CardDef` script aligned with `spirit/tools/import_set.py` conventions (GUID via `uuid5(DNS, "spirit.ptcgo." + catalogId)`).

## Prefab UI

For each attack, ability, or Trainer effect:

1. Enter effect text and click **Match from text**, or
2. Manually **Add** a prefab from the dropdown and edit parameters.

Then click **Generate card** and copy the Python output.

## Save / new sets

Saving a card:

1. Writes the Python script under `spirit/game/scripts/cards/<SET>/`
2. Downloads art to `spirit/assets/cards/<SET>/`
3. If `<SET>` is missing from `sets.json`, registers it (block, externalId/ptcgoCode, count) and adds it to the appropriate entries in `formats.json` (Expanded always; Standard for modern SV/SWSH-era sets; Legacy for BW)

Existing files require confirmation before overwrite.

## Reprints

When another printing of the same card name already exists — in this set or another format — enable **Save as a Spirit reprint() stub** to emit:

```python
from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH9/UltraBall_150.py"),
               collector_number=..., rarity=...,
               set_code="SV09", key="SV09")
```

Same-set secret rares still use a local sibling filename with no `set_code` override.
