"""Shuckle (SV3 5 -- JP SV3 005; English OBF/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="593d8b55-792f-528b-9d58-7a632d72ed20",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Attack(
            title="Berry Scent",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=pc.protect_next_turn(reduce=30),
        ),
    ],
)
