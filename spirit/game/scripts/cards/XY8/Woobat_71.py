"""Woobat (XY - BREAKthrough 71/162 -- JP XY9-B 027/080).

Basic Psychic Pokemon. HP 60, weakness Lightning x2, resistance Fighting
-20, retreat 1.

  Odor Sleuth  [C]  Flip a coin. If heads, put a card from your discard
                    pile into your hand.
  Psyshot  [P] 10
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef


async def odor_sleuth(ctx):
    heads = await ctx.flip_coins(1, "Odor Sleuth")
    if not (heads and heads[0]):
        return
    cards = list(ctx.discard_pile())
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1,
                                   prompt="Choose a card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="7b73f650-0491-5174-8aa1-744bc4d5599d",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    display_name="Woobat",
    searchable_by=["Woobat", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=527,
    abilities=[
        Attack(title="Odor Sleuth",
               game_text="Flip a coin. If heads, put a card from your discard pile into your hand.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0, effect=odor_sleuth),
        Attack(title="Psyshot", game_text="", cost={PokemonTypes.PSYCHIC: 1}, damage=10),
    ],
)
