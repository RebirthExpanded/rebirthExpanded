"""Gloom (SM - Unbroken Bonds 7/214).

Stage 1 Grass Pokemon. HP 80, weakness Fire x2, no resistance, retreat 2.

  Ability  Irresistible Aroma  Once during your turn (before your attack),
                               if your opponent's Bench isn't full, you may
                               flip a coin. If heads, your opponent reveals
                               their hand. Put a Basic Pokemon you find
                               there onto their Bench.

  Drool [GC] 30

The Bench clause is printed, so it is the Ability's condition; their hand
being empty is the other half of "nothing to do", and hand SIZE is public,
so asking for it leaks nothing. What is in the hand stays hidden until the
coin comes up heads and the reveal happens.

The Basic goes onto THEIR Bench, and bench_pokemon files a card under its
own owner, so it lands on the right side by itself.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _irresistible_aroma_condition(board, player_id, pokemon=None):
    """Their Bench has room, and they are holding something."""
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    bench = board.find_player_area(opponent, "bench")
    hand = board.find_player_area(opponent, "hand")
    if bench is None or hand is None or not hand.children:
        return False
    return len(bench.children) < effective_bench_capacity(board, opponent)


async def irresistible_aroma(ctx):
    """Coin; on heads, bench a Basic out of the opponent's revealed hand."""
    heads, = await ctx.flip_coins(1, "Irresistible Aroma")
    if not heads:
        return
    hand = await ctx.reveal_hand(ctx.opponent_id)
    basics = [c for c in hand if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(
        basics, 1, prompt="Choose a Basic Pokémon to put onto their Bench.")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = PokemonCardDef(
    guid="4bb8e014-e7c7-5eaa-8169-0b59beda126a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Irresistible Aroma",
            game_text=(
                "Once during your turn (before your attack), if your "
                "opponent's Bench isn't full, you may flip a coin. If heads, "
                "your opponent reveals their hand. Put a Basic Pokémon you "
                "find there onto their Bench."
            ),
            activation=Activations.ONCE_PER_TURN,
            condition=_irresistible_aroma_condition,
            effect=irresistible_aroma,
        ),
        Attack(
            title="Drool",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
