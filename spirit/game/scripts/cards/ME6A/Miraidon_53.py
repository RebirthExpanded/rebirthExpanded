"""Miraidon (ME6A 53 -- JP M6a 053; English 30C/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c35aa910-ffaa-519d-b70d-4e95917f0a64",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="Mach Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Electro Drift",
            game_text="Discard 2 Lightning Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=ac.self_energy_discard_attack(count=2, energy_type=PokemonTypes.LIGHTNING),
        ),
    ],
)
