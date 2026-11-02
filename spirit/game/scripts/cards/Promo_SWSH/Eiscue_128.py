"""Eiscue (Promo_SWSH 128 -- JP SP 173; English SP/128). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card


def _water_energy_card(card):
    return is_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def _ice_bonus(ctx):
    if not any(_water_energy_card(c) for c in ctx.hand()):
        return
    gone = await ctx.discard_from_hand(1, minimum=0, predicate=_water_energy_card,
                                       prompt="Discard a Water Energy card to draw 3 cards")
    if gone:
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="0d0012dd-e871-5cf2-9f32-7f710aece478",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Ice Bonus",
            game_text="Discard a Water Energy card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=_ice_bonus,
        ),
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
