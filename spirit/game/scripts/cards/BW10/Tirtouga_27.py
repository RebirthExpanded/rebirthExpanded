"""Tirtouga (BW - Plasma Blast 27/101 -- JP BW9-B 021/076, the art here).

Restored Water Pokemon. HP 90, weakness Grass x2, no resistance,
retreat 3.

  Ability  Prehistoric Call  Once during your turn (before your attack),
                             if this Pokemon is in your discard pile, you
                             may put this Pokemon on the bottom of your
                             deck.
  Slam [WCC] 30x  Flip 2 coins. This attack does 30 damage times the
                  number of heads.

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
from spirit.game.card_effects.attacks_common import flip_damage


async def prehistoric_call(ctx):
    if not await ctx.ask_yes_no("Put this Pokémon on the bottom of your deck?"):
        return
    await ctx.put_on_bottom_of_deck(ctx.source)



card = PokemonCardDef(
    guid="eaab6b55-3952-537c-800f-533b0ab5604b",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    display_name="Tirtouga",
    searchable_by=["Tirtouga", "Restored"],
    subtypes=["Restored"],
    collector_number=27,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.RESTORED,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    
    family_id=564,
    abilities=[
        Ability(title="Prehistoric Call",
                game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put this Pokémon on the bottom of your deck.",
                activation=Activations.ONCE_PER_TURN,
                usable_from="discard",
                effect=prehistoric_call),
        Attack(title="Slam", game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
               damage=30, damage_operator="x", effect=flip_damage(coins=2, per_heads=30)),
    ],
)
