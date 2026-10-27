"""Pineco (SV10 4 -- JP SV10 001; English DRI/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="06971a37-afe1-5089-8852-f8512b9e6726",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Attack(
            title="Hang Down",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
