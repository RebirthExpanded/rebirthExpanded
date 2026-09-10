"""Naganadel-GX (SM - Forbidden Light 56/131).

Stage 1 Psychic Pokemon-GX, Ultra Beast, evolves from Poipole. HP 210,
weakness Psychic x2, no resistance, retreat 1.

  Beast Raid   [C]   20x  20 damage for each of your Ultra Beasts in play.
  Jet Needle   [PCC] 110  This attack's damage isn't affected by Weakness
                          or Resistance.
  Stinger-GX   [CCC]      Both players shuffle their Prize cards into their
                          decks. Then, each player puts the top 3 cards of
                          their deck face down as their Prize cards. (You
                          can't use more than 1 GX attack in a game.)

Stinger-GX resets the game to a 3-prize race for BOTH players, so the
loop runs over both and the prize count is SET to what was dealt rather
than added to it -- board.prizes_dealt is a running total everywhere else,
and leaving it at 6+3 would make prizes_taken read 6 and the pile's gap
rendering wrong.

Face-up Prizes make no difference to the first half: the attack shuffles
"your Prize cards", not your face-down ones, so a pile Town Map turned
over goes into the deck like any other. They come back face down, which
needs no code -- move_card clears face_up whenever a card changes zone.

Beast Raid counts Ultra Beasts, the subtype Marshadow's Red Knuckles was
already written against before any card in the pool carried it.

Jet Needle waives Weakness and Resistance and nothing else, so it is a
plain deal_damage with both flags rather than ignore_effects_attack.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per

PRIZES_AFTER_STINGER = 3


def _ultra_beasts_in_play(ctx) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play()
               if "Ultra Beast" in subtypes_for(p.archetype_id))


async def jet_needle(ctx):
    """110, unaffected by Weakness or Resistance."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)


async def stinger_gx(ctx):
    """Both players shuffle their Prizes back and lay out 3 new ones."""
    board = ctx.board
    for pid in (ctx.player_id, ctx.opponent_id):
        area = board.find_player_area(pid, "prizePile")
        if area is None:
            continue
        # "their Prize cards" -- face up or not; they go back face down,
        # which move_card handles on the way in and out.
        await ctx.shuffle_into_deck(list(area.children), pid)
        dealt = board.deal_from_deck(pid, "prizePile", PRIZES_AFTER_STINGER)
        for entry in dealt:
            ctx._queue(ctx.session._entity_moved_msg(
                entry["entity_id"], entry["destination_id"], entry["position"]))
        # deal_from_deck ADDS to the running total; this attack replaces the
        # spread, so the count is the pile itself.
        board.prizes_dealt[pid] = len(area.children)
        ctx._queue(ctx.session._refresh_prize_gaps(pid, area))


card = PokemonCardDef(
    guid="418afad7-d506-5514-944a-a62ba7072547",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGX.Name",
    display_name="Naganadel-GX",
    searchable_by=["Naganadel-GX", "Stage 1", "GX", "Ultra Beast",
                   "NaganadelGX"],
    subtypes=["Stage 1", "GX", "Ultra Beast"],
    collector_number=56,
    set_code="SM6",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    family_id=803,
    abilities=[
        Attack(
            title="Beast Raid",
            game_text="This attack does 20 damage for each of your Ultra Beasts in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(_ultra_beasts_in_play, 20),
        ),
        Attack(
            title="Jet Needle",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=jet_needle,
        ),
        Attack(
            title="Stinger-GX",
            game_text="Both players shuffle their Prize cards into their decks. Then, each player puts the top 3 cards of their deck face down as their Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            gx=True,
            effect=stinger_gx,
        ),
    ],
)
