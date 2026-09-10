"""Alolan Muk (SM - Sun & Moon 58/149 -- JP SM1M 023/060).

Stage 1 Psychic. HP 120, weakness Psychic x2, retreat 4. Evolves from
Alolan Grimer.

  Ability  Power of Alchemy  Each Basic Pokemon in play, in each player's
                             hand, and in each player's discard pile has no
                             Abilities.

  Crunch  [PPCC] 90  Flip a coin. If heads, discard an Energy from your
                     opponent's Active Pokemon.

Silent Lab as an Ability. The lock is word-for-word the Stadium's, so it
is the same passive: blocks_abilities for the board and
blocks_out_of_play_abilities for the hands and discard piles, the second
existing because every other lock in the game stops at "in play".

The difference is what can switch it off. A Stadium passive answers to
nothing; this one is a Pokemon Ability, so an ability lock (Path to the
Peak, Garbotoxin, another Alolan Muk is not one -- it is a Stage 1) turns
it off, and it turns off both players' Basics while it is on, Tapu Lele-GX
and Dedenne-GX included.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import SilentLabPassive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

CRUNCH = "Crunch"


async def crunch(ctx):
    """90, then heads discards an Energy from the Defending Pokemon."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, CRUNCH)
    if not heads or not heads[0]:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose Energy to discard from the Defending Pokémon")

card = PokemonCardDef(
    guid="b46283bc-46ac-5f45-aec0-d6f044f5ebad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMuk.Name",
    display_name="Alolan Muk",
    searchable_by=["Alolan Muk", "Stage 1", "AlolanMuk"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Power of Alchemy",
            game_text="Each Basic Pokémon in play, in each player's hand, and in each player's discard pile has no Abilities.",
            passive=SilentLabPassive(),
        ),
        Attack(
            title=CRUNCH,
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=crunch,
        ),
    ],
)
