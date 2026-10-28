"""Riolu (SV1 113 -- JP SV1S 040; English PAF/173, SVI/113, SVI/215). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2dae4f95-7de8-51ff-bb49-b3fe90655ff5",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu", "Basic"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Attack(
            title="Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.recoil_attack(20),
        ),
    ],
)
