"""Rapidash (SM - Team Up 18/181 -- JP SM9 017/095).

Stage 1 Fire Pokemon, evolves from Ponyta. HP 100, weakness Water x2,
retreat 1.

  Searing Flame  [R] 20   Your opponent's Active Pokemon is now Burned.
  Agility        [RR] 60  Flip a coin. If heads, prevent all effects of
                          attacks, including damage, done to this Pokemon
                          during your opponent's next turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import flip_protection
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="dab4975c-9f13-558f-8cd9-b714ef4e491a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Attack(title="Searing Flame",
               game_text="Your opponent's Active Pokémon is now Burned.",
               cost={PokemonTypes.FIRE: 1}, damage=20,
               effect=condition_attack(SpecialConditions.BURNED)),
        Attack(title="Agility",
               game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
               cost={PokemonTypes.FIRE: 2}, damage=60,
               effect=flip_protection(prevent=True, effects_too=True)),
    ],
)
