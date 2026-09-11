"""Wishful Baton (SM - Burning Shadows 128/147 -- JP SMN 017/025, the art here).

Pokemon Tool.

  "If the Pokemon this card is attached to is your Active Pokemon and is
   Knocked Out by damage from an opponent's attack, move up to 3 basic
   Energy cards from that Pokemon to 1 of your Benched Pokemon."

ON_KNOCKED_OUT_IN_PLAY (see Heavy Baton); all the chosen Energy goes to
one bencher.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers


async def wishful_baton(ctx):
    holder = ctx.source
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    bench = ctx.my_bench()
    pool = [e for e in ctx.attached_energies(holder) if is_basic_energy_card(e)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(3, len(pool)), minimum=0,
        prompt="Choose up to 3 basic Energy cards to move to 1 of your Benched Pokémon")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if target is None:
        target = bench[0]
    for energy in picks:
        await ctx.move_energy(energy, target)


card = PokemonToolCardDef(
    guid="0e7a336b-b0e1-5539-9778-8d5910b426b0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WishfulBaton.Name",
    display_name="Wishful Baton",
    searchable_by=["Wishful Baton", "Item", "Pokémon Tool", "WishfulBaton"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=128,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Wishful Baton",
            game_text="If the Pokémon this card is attached to is your Active Pokémon and is Knocked Out by damage from an opponent's attack, move up to 3 basic Energy cards from that Pokémon to 1 of your Benched Pokémon.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=wishful_baton,
        ),
    ],
)
