"""Volcanion (ME3 25 -- JP M3 024; English POR/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5f5a0b49-ae40-5fc6-96b3-09e47e9b114c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=721,
    abilities=[
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Powerful Steam",
            game_text="Flip a coin for each Water Energy attached to this Pokémon. This attack does 90 damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=ac.flip_damage(per_heads=90, coins_from=ac.count_energy("self", PokemonTypes.WATER)),
        ),
    ],
)
