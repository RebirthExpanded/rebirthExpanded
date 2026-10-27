"""N's Purrloin (SV09 96 -- JP SV9 059; English JTG/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def thieving_swipe(ctx):
    await ctx.deal_damage()
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Choose a card to put on the bottom of your opponent's deck")
    if picks:
        await ctx.put_on_bottom_of_deck(picks[0])


card = PokemonCardDef(
    guid="d6ce618c-5371-58ff-ba42-10cf43a9d1b9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsPurrloin.Name",
    display_name="N's Purrloin",
    searchable_by=["N's Purrloin", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Thieving Swipe",
            game_text="Your opponent reveals their hand, and you choose a card you find there and put it on the bottom of their deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=thieving_swipe,
        ),
    ],
)
