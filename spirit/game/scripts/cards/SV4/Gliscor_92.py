"""Gliscor (SV4 92 -- JP SV3a 023; English PAR/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1e05cb37-3622-514f-b04e-46f4d9c4db1c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Toxic Sting",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 2 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.POISONED, flip=True, counters=2),
        ),
    ],
)
