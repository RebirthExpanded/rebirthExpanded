"""Cetitan (SVP 63 -- JP SVP 058; English SVP/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="65be3860-c913-509f-85ba-9827af0b2831",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Attack(
            title="Avalanche",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=ac.spread_damage(10, also_base=True),
        ),
        Attack(
            title="Rolling Slider",
            game_text="Flip 3 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=100),
        ),
    ],
)
