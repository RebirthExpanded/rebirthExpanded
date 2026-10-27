"""Clefairy (ME3 30 -- JP M3 029; English POR/30, POR/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="c4a1eae0-65ab-5818-aa18-d57ab9ce0c99",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=173,
    abilities=[
        Attack(
            title="Follow Me",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.gust_attack(),
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)
