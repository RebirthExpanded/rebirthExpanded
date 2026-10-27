"""Snom (ME2PT5 52 -- JP M2a 040; English ASC/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4427f5cd-0dc2-5a2e-af56-6a005a3cc895",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    display_name="Snom",
    searchable_by=["Snom", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=872,
    abilities=[
        Attack(
            title="Icicle",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
