"""Pokemon Card Gym Medal (JP XY-P, Gym Leader tournament prize -- no
English print; the number 901 is a pool-local slot in the XY promos).

Item.

  "Choose 1 of your face-down Prize cards, look at it, and put it back.
   You may switch that Prize card with the top card of your deck."

Only the owner sees the card; whether it is switched or not, it stays face
down for everyone afterwards.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import has_face_down_prize
from spirit.game.data_utils import ItemCardDef


async def pokemon_card_gym_medal(ctx):
    await ctx.swap_prize_with_deck_top(
        look_first=True, prompt="Choose a Prize card to look at.")


card = ItemCardDef(
    guid="4a97cd00-3f47-5846-be91-3adeabee1194",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCardGymMedal.Name",
    display_name="Pokémon Card Gym Medal",
    searchable_by=["Pokémon Card Gym Medal", "Gym Medal", "Item"],
    subtypes=["Item"],
    collector_number=901,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    condition=has_face_down_prize,
    effect=pokemon_card_gym_medal,
)
