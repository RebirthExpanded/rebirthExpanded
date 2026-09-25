"""Pidgey (SM - Team Up 121/181 -- JP SM9 065/095).

Basic Colorless Pokemon. HP 50, weakness Lightning x2, resistance Fighting
-20, retreat 1.

  Collect  [C]     Draw a card.
  Gust     [CC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="a0f8a8e4-e55e-5892-bcfa-0d8b08a5db29",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=['Pidgey', 'Basic', 'Pidgey'],
    subtypes=['Basic'],
    collector_number=121,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=16,
    abilities=[
        Attack(title="Collect", game_text="Draw a card.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=draw_attack(1)),
        Attack(title="Gust", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
