"""Sneasel (SV - Prismatic Evolutions 61/131 -- JP SVM 075/175, the art here).

Basic Darkness Pokemon. HP 60, weakness Grass x2, no retreat cost.

  Claw Slash [D] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="1768844a-2cee-5fc1-9e98-3b98e88ce157",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    family_id=215,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
