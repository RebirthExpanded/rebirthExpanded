"""Growlithe (SV10 27 -- JP SV10 013; English DRI/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9ede5c15-d461-5994-9b10-d09323463745",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Dig Claws",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
