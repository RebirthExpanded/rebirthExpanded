"""Seel (SV035 86 -- JP SV2a 086; English MEW/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="482cce2a-32ba-5242-9a23-51ecb777594f",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel",
    searchable_by=["Seel", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Chilly",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
