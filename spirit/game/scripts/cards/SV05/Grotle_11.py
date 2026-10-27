"""Grotle (SV05 11 -- JP SV5K 004; English TEF/11, TEF/164). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="f1a7f834-8570-52b8-b950-0039e528925e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    display_name="Grotle",
    searchable_by=["Grotle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Ramming Shell",
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=pc.protect_next_turn(reduce=20),
        ),
    ],
)
