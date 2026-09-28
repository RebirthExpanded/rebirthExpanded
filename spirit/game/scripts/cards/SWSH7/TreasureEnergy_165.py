"""Treasure Energy (SWSH - Evolving Skies 165/203).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [C] Energy.
   If you took this card as a face-down Prize card during your turn, before
   you put it into your hand, you may attach this card to 1 of your
   Pokemon."

Dream Ball's ON_TAKEN_AS_PRIZE window: the session opens it only for a
face-down Prize going to hand, and the card is attached from there. A Prize
taken on the opponent's turn (a Knock Out from an attack's recoil or from
damage counters during their turn) opens nothing.
"""

from spirit.game.data_utils import EnergyCardDef, Ability, Triggers
from spirit.game.attributes import PokemonTypes, Rarities


async def treasure_energy_prize_window(ctx):
    ctx.suppress_announce = True
    board, pid = ctx.board, ctx.player_id
    if ctx.session.turn_state.active_player_id != pid:
        return
    targets = list(board.pokemon_in_play(pid))
    if not targets:
        return
    if not await ctx.ask_yes_no("Attach Treasure Energy to 1 of your Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to attach Treasure Energy to.")
    if target is not None:
        await ctx.attach_energy(ctx.source, target)


card = EnergyCardDef(
    guid="d193d412-b5e1-5751-a2ac-103c8ac26360",
    key="SWSH7",
    name="Treasure Energy",
    display_name="Treasure Energy",
    searchable_by=["Treasure Energy", "Special"],
    subtypes=["Special"],
    collector_number=165,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    abilities=[
        Ability(
            title="Treasure Energy",
            game_text="If you took this card as a face-down Prize card during your turn, before you put it into your hand, you may attach this card to 1 of your Pokémon.",
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=treasure_energy_prize_window,
        ),
    ],
)
