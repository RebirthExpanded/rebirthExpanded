"""Pansage (SV4 4 -- JP SV4K 001; English PAR/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="64e50b67-9808-5da8-b287-5b4bfd8273c3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    display_name="Pansage",
    searchable_by=["Pansage", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=511,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Leech Seed",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=su.heal_attack(10),
        ),
    ],
)
