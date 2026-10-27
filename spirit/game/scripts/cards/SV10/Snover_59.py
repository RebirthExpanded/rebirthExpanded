"""Snover (SV10 59 -- JP SV10 026; English DRI/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="07d58345-35cf-57ed-98da-d3c30ea3bd77",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=459,
    abilities=[
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Icicle",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
