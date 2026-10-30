from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card


async def pokegear_3_0(ctx):
    """Look at the top 7 cards of your deck. You may reveal a Supporter card
    you find there and put it into your hand. Shuffle the other cards back
    into your deck."""
    top = ctx.deck_top(7)
    if not top:
        return
    candidates = [c for c in top if is_supporter_card(c)]
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="You may put a Supporter into your hand.",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="be292e28-ece9-597f-bd4b-3e884acb23a1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pokégear 3.0","Item","Pokgear30"],
    subtypes=["Item"],
    collector_number=235,
    set_code="SM10",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=pokegear_3_0,
)
