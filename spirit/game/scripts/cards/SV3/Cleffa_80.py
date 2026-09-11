"""Cleffa (SV - Obsidian Flames 80/197 -- JP SV3 042/108, the art here).

Basic Psychic Pokemon. HP 30, weakness Metal x2, no resistance, retreat 0.

  Grasping Draw [no cost]  Draw cards until you have 7 cards in your hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="43f771b3-1b0c-5c7f-b1a1-d1b29d2a20f8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    family_id=173,
    abilities=[
        Attack(title="Grasping Draw",
               game_text="Draw cards until you have 7 cards in your hand.",
               cost={},
               effect=draw_until_effect(7)),
    ],
)
