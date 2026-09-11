"""Milotic (XY - Primal Clash 44/160 -- JP XY5-Bt 019/070).

Stage 1 Water Pokemon, evolves from Feebas. HP 110, weakness Grass x2,
retreat 2.

  Ability  Sparkling Ripples  When you play this Pokemon from your hand to
                              evolve 1 of your Pokemon, you may put a card
                              from your discard pile into your hand.
  Aqua Swirl  [WCC] 60  You may have your opponent switch their Active
                        Pokemon with 1 of their Benched Pokemon.

Sparkling Ripples rides ON_EVOLVE and reads the ctx's evolved_from_hand
flag, so a Wally / deck-sourced evolution does not fire it; any card at
all comes back. Aqua Swirl's switch is THEIRS to
make -- they pick the Pokemon that comes up -- and it is "you may", asked
of the attacker after the damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers)


async def sparkling_ripples(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    cards = list(ctx.discard_pile())
    if not cards:
        return
    if not await ctx.ask_yes_no("Put a card from your discard pile into your hand?"):
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1, prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


async def aqua_swirl(ctx):
    await ctx.deal_damage()
    bench = list(ctx.opponent_bench())
    defender = ctx.opponent_active()
    if not bench or defender is None or ctx.effects_blocked(defender):
        return
    if not await ctx.ask_yes_no("Have your opponent switch their Active Pokémon?"):
        return
    chosen = await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id)
    if chosen is not None:
        await ctx.switch_active(ctx.opponent_id, chosen)


card = PokemonCardDef(
    guid="bb5e4bd4-909d-5833-af0d-cfbb48f6bbe3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Sparkling Ripples",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may put a card from your discard pile into your hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=sparkling_ripples,
        ),
        Attack(
            title="Aqua Swirl",
            game_text="You may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=aqua_swirl,
        ),
    ],
)
