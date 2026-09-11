"""Shaymin-EX (XY - Roaring Skies 77/108 -- JP XY6-B 043/078).

Basic Colorless Pokemon-EX. HP 110, weakness Lightning x2, resistance
Fighting -20, retreat 1.

  Ability  Set Up  When you play this Pokemon from your hand onto your
                   Bench, you may draw cards until you have 6 cards in your
                   hand.
  Sky Return  [CC] 30  Return this Pokemon and all cards attached to it to
                       your hand.

BANNED in Expanded (pokemon.com's banned card list: 77/108, 77a/108 and
106/108), and registered as such in formats.json. It is implemented so the
card exists and shows up correctly, not so it can be played; the format
check refuses it in a deck.

Set Up is the ON_PLAY window -- a hand-to-Bench play only, so a Shaymin-EX
that reaches the Bench from the deck does not fire it. Sky Return brings
the whole pile back to hand as separate cards, and leaving the Active spot
that way promotes a new Active afterwards.

The pool's CUSTOM/1 test card carries this Ability with no name; it is a
stand-in and stays as it is.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers
from spirit.game.session.effects import full_stack


async def set_up(ctx):
    """You may draw until you hold 6 cards."""
    if ctx.hand_size() >= 6:
        return
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


async def sky_return(ctx):
    """30, then this Pokemon and everything on it go back to hand."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is None:
        return
    was_active = attacker is ctx.my_active()
    attached = [c for c in full_stack(attacker) if c is not attacker]
    if attached:
        await ctx.put_in_hand(attached, reveal=False)
    await ctx.put_in_hand([attacker], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="6d47bac7-58d3-596e-947e-ef004790d2e7",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=77,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Ability(
            title="Set Up",
            game_text="When you play this Pokémon from your hand onto your Bench, you may draw cards until you have 6 cards in your hand.",
            trigger=Triggers.ON_PLAY,
            effect=set_up,
        ),
        Attack(
            title="Sky Return",
            game_text="Return this Pokémon and all cards attached to it to your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=sky_return,
        ),
    ],
)
