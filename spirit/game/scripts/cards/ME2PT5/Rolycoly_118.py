"""Rolycoly (ME2PT5 118 -- JP M2a 095; English ASC/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9c5f60eb-b18a-5b50-aba3-02071c082788",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    display_name="Rolycoly",
    searchable_by=["Rolycoly", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=837,
    abilities=[
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
