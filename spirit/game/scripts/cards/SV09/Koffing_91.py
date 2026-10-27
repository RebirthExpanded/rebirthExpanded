"""Koffing (SV09 91 -- JP SV9 056; English JTG/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e2470229-0cc0-5fc4-a137-1dcc072e8f26",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=109,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Suffocating Gas",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
