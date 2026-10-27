"""Larry's Skill (SV085 115 -- JP SV8a 162; English PRE/115, PRE/139). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.session.effects import is_pokemon_card, is_supporter_card


async def larrys_skill(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.discard_cards(hand)
    groups = await ctx.search_deck_groups([
        (is_pokemon_card, 1, "a Pokémon"),
        (is_supporter_card, 1, "a Supporter card"),
        (is_basic_energy_card, 1, "a Basic Energy card"),
    ], prompt="Choose a Pokémon, a Supporter card, and a Basic Energy card.")
    picks = [c for g in groups for c in g]
    if picks:
        await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="3e2d4e86-946d-543f-90b3-0bb436af36c5",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LarrysSkill.Name",
    display_name="Larry's Skill",
    searchable_by=["Larry's Skill", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=larrys_skill,
)
