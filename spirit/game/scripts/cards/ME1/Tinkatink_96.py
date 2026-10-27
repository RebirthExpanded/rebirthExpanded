"""Tinkatink (ME1 96 -- JP M1L 048; English MEG/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3bc0ec25-b1ff-5918-9aec-be857e7bdf3c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=957,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)
