"""Charmeleon (SM - Team Up 13/181 -- JP SM9 012/095).

Stage 1 Fire Pokemon, evolves from Charmander. HP 90, weakness Water x2,
retreat 2.

  Fire Fang  [RR] 30  Your opponent's Active Pokemon is now Burned.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="76e5aeb5-a346-5c53-b3d5-e125db9e0efe",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(title="Fire Fang",
               game_text="Your opponent's Active Pokémon is now Burned.",
               cost={PokemonTypes.FIRE: 2}, damage=30,
               effect=condition_attack(SpecialConditions.BURNED)),
    ],
)
