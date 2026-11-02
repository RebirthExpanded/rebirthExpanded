"""Ice Rider Calyrex V (Promo_SWSH 130 -- JP SP3 001; English SP/130). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fc16d6f5-26b6-5ce8-9b32-752ed4bc210b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name",
    display_name="Ice Rider Calyrex V",
    searchable_by=["Ice Rider Calyrex V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=130,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=898,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.spread_damage(10, also_base=True),
        ),
        Attack(
            title="Frost Stamp",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
