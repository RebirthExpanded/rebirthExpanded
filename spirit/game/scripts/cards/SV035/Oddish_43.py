"""Oddish (SV035 43 -- JP SV2a 043; English MEW/43, PAF/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="72ecc1de-23a7-5856-806a-c49fcad65d5b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Razor Leaf",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
