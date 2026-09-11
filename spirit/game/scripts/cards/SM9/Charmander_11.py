"""Charmander (SM - Team Up 11/181 -- JP SM9 010/095).

Basic Fire Pokemon. HP 50, weakness Water x2, retreat 1.

  Scratch   [R] 10
  Reprisal  [CC] 20x  This attack does 20 damage for each damage counter
                      on this Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="d8f3c361-18d6-559b-95b4-df12c41e5320",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(title="Scratch", game_text="", cost={PokemonTypes.FIRE: 1}, damage=10),
        Attack(title="Reprisal",
               game_text="This attack does 20 damage for each damage counter on this Pokémon.",
               cost={PokemonTypes.COLORLESS: 2}, damage=20,
               effect=damage_per(damage_counters_on("self"), 20)),
    ],
)
