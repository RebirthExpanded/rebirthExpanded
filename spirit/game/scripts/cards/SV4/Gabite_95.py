"""Gabite (SV4 95 -- JP SV3a 028; English PAR/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="567d71bc-8b12-556f-a2c7-6f96281d5133",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=["Gabite", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
