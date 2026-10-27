"""Ponyta (SV07 19 -- JP SVI 007; English SCR/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8b2fb777-a243-55f2-88bc-b9ab7e4baf8d",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
