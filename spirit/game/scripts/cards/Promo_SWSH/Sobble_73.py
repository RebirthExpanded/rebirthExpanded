"""Sobble (Promo_SWSH 73 -- JP SP 008; English SP/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="888dcf13-be5d-55a3-a98a-09383eb39cfb",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    display_name="Sobble",
    searchable_by=["Sobble", "Basic"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=816,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.debuff_defender_attacks(20),
        ),
        Attack(
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
