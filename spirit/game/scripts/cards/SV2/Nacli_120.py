"""Nacli (SV2 120 -- JP SV2D 045; English PAL/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d8eefb06-a18c-543b-a85d-31ab88c1bb55",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    display_name="Nacli",
    searchable_by=["Nacli", "Basic"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=932,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
