"""Diglett (SV035 50 -- JP SV2a 050; English MEW/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e4b0e7e0-c299-5576-9266-0e0a57e52d04",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
