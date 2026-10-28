"""Bombirdier (SV2 147 -- JP SV2D 056; English PAL/147). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="00f8160d-c978-5b27-8217-2a8ef3709a95",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=962,
    abilities=[
        Attack(
            title="Delivery Pocket",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Dark Edge",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
