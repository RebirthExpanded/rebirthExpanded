"""Mega Sableye & Tyranitar-GX (SM - Unified Minds 126/236 -- JP SM11 054/094).

Basic Darkness TAG TEAM Pokemon-GX. HP 280, weakness Fighting x2,
resistance Psychic -20, retreat 4.

  Greed Crush  [DDDDC] 210  If a Pokemon-GX or Pokemon-EX is Knocked Out by
                            damage from this attack, take 1 more Prize card.
  Giga Fall-GX [DDDDC] 250  If this Pokemon has at least 5 extra Energy
                            attached to it (in addition to this attack's
                            cost), discard the top 15 cards of your
                            opponent's deck.

Greed Crush rides the bonus-prize watch Sky Seal Stone's Star Order added:
a this-turn entry that resolve_knockouts consults on attack-damage
knockouts, with the target filter deciding which knockouts pay. Damage from
THIS attack is what the card asks for, so the watch is registered inside
the attack and cleared at the next begin_turn like the rest.

Giga Fall-GX's 15-card mill takes what is there when the deck holds fewer;
the deck-out itself is checked at the start of a turn, not here.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef, subtypes_for
from spirit.game.session.legal_actions import attack_cost_satisfied

MILL = 15
# The printed cost plus the five extra Energy, asked as a single question.
_COST_PLUS_EXTRAS = {"Darkness": 4, "Colorless": 6}


def _is_gx_or_uppercase_ex(pokemon) -> bool:
    """"Pokemon-GX or Pokemon-EX": the SM/XY-era rule boxes, not SV's ex."""
    return any(s in ("GX", "EX") for s in subtypes_for(pokemon.archetype_id))


async def greed_crush(ctx):
    """210, and a GX or EX knocked out by it is worth one more Prize."""
    ctx.add_extra_prize_watcher(target_predicate=_is_gx_or_uppercase_ex,
                                prizes=1)
    await ctx.deal_damage()


async def giga_fall_gx(ctx):
    """250, and with 5 extra Energy attached, 15 cards off their deck."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board):
        await ctx.discard_cards(ctx.deck_top(MILL, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="6ece154a-c9fc-565c-98da-35a8b4d47041",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSableyeTyranitarGX.Name",
    display_name="Mega Sableye & Tyranitar-GX",
    searchable_by=["Mega Sableye & Tyranitar-GX", "Basic", "TAG TEAM", "GX",
                   "MegaSableyeTyranitarGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=126,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=302,
    abilities=[
        Attack(
            title="Greed Crush",
            game_text="If a Pokémon-GX or Pokémon-EX is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.DARKNESS: 4, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=greed_crush,
        ),
        Attack(
            title="Giga Fall-GX",
            game_text="If this Pokémon has at least 5 extra Energy attached to it (in addition to this attack's cost), discard the top 15 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 4, PokemonTypes.COLORLESS: 1},
            damage=250,
            gx=True,
            effect=giga_fall_gx,
        ),
    ],
)
