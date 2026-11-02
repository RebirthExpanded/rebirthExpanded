"""Blastoise V (Promo_SWSH 101 -- JP SEK 001; English SP/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3aa49ecc-de86-57a8-a3a7-4ee55c16947e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseV.Name",
    display_name="Blastoise V",
    searchable_by=["Blastoise V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=101,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=9,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Torrential Cannon",
            game_text="During your next turn, this Pokémon can't use Torrential Cannon.",
            cost={PokemonTypes.WATER: 3},
            damage=200,
            locks_next_turn=True,
        ),
    ],
)
