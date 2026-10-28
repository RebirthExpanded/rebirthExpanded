"""Patrol Cap (SV3 191 -- JP SV3 101; English OBF/191). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.attributes import AttrID
from spirit.game.session.passives import carrier_pokemon


class PatrolCapPassive(Passive):
    """Holder Active: the opponent's effects can't discard your deck."""

    def blocks_discard(self, card, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder.parent is None or holder.parent.get_attribute(AttrID.NAME) != "activePokemonArea":
            return False
        if card.owning_player_id != holder.owning_player_id:
            return False
        parent = getattr(card, "parent", None)
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "deck"


card = PokemonToolCardDef(
    guid="a1ab969e-8da7-5aae-a69f-37026785ef39",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PatrolCap.Name",
    display_name="Patrol Cap",
    searchable_by=["Patrol Cap", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=191,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=PatrolCapPassive(),
)
