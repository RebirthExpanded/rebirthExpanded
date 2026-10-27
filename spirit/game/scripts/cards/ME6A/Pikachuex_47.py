"""Pikachu ex (ME6A 47 -- JP M6a 047; English 30C/149, 30C/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="44db17a0-6d76-5a8d-b731-891aecadb26b",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=47,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Pika-Pika Parade",
            game_text="Search your deck for any number of Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=8, prompt="Choose any number of Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
