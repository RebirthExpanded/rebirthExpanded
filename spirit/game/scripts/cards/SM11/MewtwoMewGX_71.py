"""Mewtwo & Mew-GX (SM - Unified Minds 71/236 -- JP SM11 029/094).

Basic Psychic TAG TEAM Pokemon-GX. HP 270, weakness Psychic x2, no
resistance, retreat 2.

  Ability  Perfection  This Pokemon can use the attacks of any Pokemon-GX
                       or Pokemon-EX on your Bench or in your discard pile.
                       (You still need the necessary Energy to use each
                       attack.)

  Miraculous Duo-GX  [PPC] 200  If this Pokemon has at least 1 extra Energy
                                attached to it (in addition to this attack's
                                cost), heal all damage from all of your
                                Pokemon.

Perfection is the borrowed-attacks passive with two sources at once -- your
Bench and your discard pile -- and the GX/EX filter over both. Everything
else follows from that: the Attack objects are the source cards' own, so a
copied GX attack still answers to the once-per-game rule, and the Energy
cost is the copied attack's own rather than this Pokemon's.

"Pokemon-GX or Pokemon-EX" is the SM/XY-era pair the pool reads elsewhere
(Counter Energy, Electrode-GX, Umbreon & Darkrai-GX), so a Scarlet & Violet
Pokemon ex in the discard lends nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import (BorrowedAttacksPassive,
                                              own_bench_pokemon,
                                              own_discard_cards)
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    subtypes_for)
from spirit.game.session.legal_actions import attack_cost_satisfied

# The [PPC] cost plus the one extra Energy, asked as a single question.
_COST_PLUS_EXTRA = {"Psychic": 2, "Colorless": 2}


def _is_gx_or_uppercase_ex(card) -> bool:
    return any(s in ("GX", "EX") for s in subtypes_for(card.archetype_id))


def _bench_and_discard(board, pokemon):
    return own_bench_pokemon(board, pokemon) + own_discard_cards(board, pokemon)


async def miraculous_duo_gx(ctx):
    """200, and with an extra Energy attached, your whole side heals."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        return
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(ctx.max_hp(pokemon), target=pokemon)


card = PokemonCardDef(
    guid="71c1a7a3-d221-5be0-959d-35c1fe486cee",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoMewGX.Name",
    display_name="Mewtwo & Mew-GX",
    searchable_by=["Mewtwo & Mew-GX", "Basic", "TAG TEAM", "GX", "MewtwoMewGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=71,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Perfection",
            game_text="This Pokémon can use the attacks of any Pokémon-GX or Pokémon-EX on your Bench or in your discard pile. (You still need the necessary Energy to use each attack.)",
            passive=BorrowedAttacksPassive(_bench_and_discard,
                                           _is_gx_or_uppercase_ex),
        ),
        Attack(
            title="Miraculous Duo-GX",
            game_text="If this Pokémon has at least 1 extra Energy attached to it (in addition to this attack's cost), heal all damage from all of your Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            gx=True,
            effect=miraculous_duo_gx,
        ),
    ],
)
