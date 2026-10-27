"""Drilbur (ZSV10PT5 45 -- JP SV11B 048; English BLK/124, BLK/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="60f6480d-a581-506f-9cce-d21d5d7f0170",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=529,
    abilities=[
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
