"""Scyther (SV05 1 -- JP SV5M 001; English TEF/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="130651ec-6e19-57d5-8e3c-1a091bdf0afa",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=123,
    abilities=[
        Attack(
            title="Cut Up",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pokémon can't use Slashing Strike.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            locks_next_turn=True,
        ),
    ],
)
