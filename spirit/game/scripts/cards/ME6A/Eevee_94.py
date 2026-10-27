"""Eevee (ME6A 94 -- JP M6a 094; English 30C/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card


async def fetch_and_hide(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    items = [c for c in hand if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(items, 1, minimum=1, prompt="Choose an Item card to put on the bottom of your opponent's deck")
    if picks:
        await ctx.put_on_bottom_of_deck(picks[0])


card = PokemonCardDef(
    guid="b4f8768a-f14e-5cac-87de-4803d95a1a8d",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Fetch and Hide",
            game_text="Your opponent reveals their hand, and you put an Item card you find there on the bottom of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=fetch_and_hide,
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
