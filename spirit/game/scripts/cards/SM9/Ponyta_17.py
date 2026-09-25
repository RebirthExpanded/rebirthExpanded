"""Ponyta (SM - Team Up 17/181 -- JP SM9 016/095).

Basic Fire Pokemon. HP 70, weakness Water x2, retreat 1.

  Live Coal  [R] 10
  Stomp      [RR] 10+  Flip a coin. If heads, this attack does 30 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="eab13329-4b1c-53f2-a7f6-fb62eabe8c66",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(title="Live Coal", game_text="", cost={PokemonTypes.FIRE: 1}, damage=10),
        Attack(title="Stomp",
               game_text="Flip a coin. If heads, this attack does 30 more damage.",
               cost={PokemonTypes.FIRE: 2}, damage=10, damage_operator="+",
               effect=flip_bonus(30)),
    ],
)
