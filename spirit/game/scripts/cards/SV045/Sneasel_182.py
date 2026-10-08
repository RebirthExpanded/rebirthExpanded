"""Sneasel (SV - Paldean Fates 182/091 -- JP SV4a 119/190, the art here).

Basic Darkness Pokemon. HP 70, weakness Grass x2, retreat 1.

  Dig Claws [D] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="9447b55b-2be2-5d50-9eea-431bfd38572f",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic"],
    subtypes=["Basic"],
    collector_number=182,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=215,
    abilities=[
        Attack(
            title="Dig Claws",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
