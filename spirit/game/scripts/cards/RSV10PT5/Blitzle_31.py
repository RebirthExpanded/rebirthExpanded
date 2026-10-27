"""Blitzle (RSV10PT5 31 -- JP SV11W 028; English WHT/114, WHT/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="787a8bbc-5c55-587f-b415-570dbd31c441",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=522,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Zap Kick",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
