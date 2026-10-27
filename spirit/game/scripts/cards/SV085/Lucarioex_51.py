"""Lucario ex (SV085 51 -- JP SVM 065; English PRE/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="a97d4df1-b4d5-541c-a436-0b8f78848a14",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucarioex.Name",
    display_name="Lucario ex",
    searchable_by=["Lucario ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=51,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Aura Uppercut",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
        ),
        Attack(
            title="Tornado Rush",
            game_text="During your next turn, this Pokémon's Tornado Rush attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=pc.boost_own_next_turn(100, "Tornado Rush"),
        ),
    ],
)
