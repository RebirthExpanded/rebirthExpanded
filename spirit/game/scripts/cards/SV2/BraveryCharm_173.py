"""Bravery Charm (SV - Paldea Evolved 173/193 -- JP SV2D 067/071).

Pokemon Tool.  "The Basic Pokemon this card is attached to gets +50 HP."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.effects import is_basic_pokemon_in_play

card = PokemonToolCardDef(
    guid="04871f7d-9452-5fcd-94e3-fbd10f2829a6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveryCharm.Name",
    display_name="Bravery Charm",
    searchable_by=["Bravery Charm", "Pokémon Tool", "BraveryCharm"],
    subtypes=["Pokémon Tool"],
    collector_number=173,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    passive=hp_bonus_tool(50, holder_pred=is_basic_pokemon_in_play),
)
