"""Lileep (BW - Plasma Blast 3/101 -- JP BW9-B 003/076, the art here).

Restored Grass Pokemon. HP 80, weakness Fire x2, resistance Water -20,
retreat 2.

  Ability  Prehistoric Call  Once during your turn (before your attack),
                             if this Pokemon is in your discard pile, you
                             may put this Pokemon on the bottom of your
                             deck.
  Spiral Drain [GC] 20  Heal 10 damage from this Pokemon.

A RESTORED Pokemon (BW Plasma Blast): not a Basic -- it can't be played
from the hand, placed at setup or found by "Basic Pokemon" searches (the
stage check does all of that) -- it comes into play only through the
Fossil Items that read "put a <name> from the top of your deck onto your
Bench", and evolves into its Stage 1 normally. Prehistoric Call is a
discard-pile Ability (usable_from="discard"), so Garbotoxin's out-of-play
half switches it off.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef



async def prehistoric_call(ctx):
    if not await ctx.ask_yes_no("Put this Pokémon on the bottom of your deck?"):
        return
    await ctx.put_on_bottom_of_deck(ctx.source)

async def spiral_drain(ctx):
    """20, then heal 10 from this Pokemon."""
    await ctx.deal_damage()
    await ctx.heal(10, ctx.attacker)


card = PokemonCardDef(
    guid="54ff6edc-c9a7-5bcd-b249-839f73d5ef4d",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Restored"],
    subtypes=["Restored"],
    collector_number=3,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.RESTORED,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER, resistance_amount=20,
    family_id=345,
    abilities=[
        Ability(title="Prehistoric Call",
                game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put this Pokémon on the bottom of your deck.",
                activation=Activations.ONCE_PER_TURN,
                usable_from="discard",
                effect=prehistoric_call),
        Attack(title="Spiral Drain", game_text="Heal 10 damage from this Pokémon.",
               cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
               damage=20, effect=spiral_drain),
    ],
)
