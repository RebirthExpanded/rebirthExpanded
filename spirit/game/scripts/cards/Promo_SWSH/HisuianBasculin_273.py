"""Hisuian Basculin (Promo_SWSH 273 -- JP SP 279; English SP/273). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects.trainers import second_players_first_turn


card = PokemonCardDef(
    guid="c76782fa-8211-56b9-a99c-09382b38fd1e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    display_name="Hisuian Basculin",
    searchable_by=["Hisuian Basculin", "Basic"],
    subtypes=["Basic"],
    collector_number=273,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Submerge Silently",
            game_text="You can use this attack only if you go second, and only during your first turn. During your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.protect_next_turn(prevent=True),
            condition=second_players_first_turn,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
