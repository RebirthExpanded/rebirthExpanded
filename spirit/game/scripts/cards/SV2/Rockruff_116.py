"""Rockruff (SV2 116 -- JP SV1a 049; English PAL/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="06136beb-e8ce-5fa2-b05c-8ee8e2e68c31",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Rock Throw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
