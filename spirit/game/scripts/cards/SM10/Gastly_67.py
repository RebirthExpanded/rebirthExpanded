"""Gastly (SM - Unbroken Bonds 67/214 -- JP SM10 030/095, the art here).

Basic Psychic Pokemon. HP 40, weakness Darkness x2, resistance Fighting
-20, retreat 1.

  Ability: Swelling Spite  When this Pokemon is Knocked Out, search your
                           deck for up to 2 Haunter and put them onto your
                           Bench. Then, shuffle your deck.
  Will-O-Wisp [CC] 20

A Knock Out effect (ON_KNOCKED_OUT_IN_PLAY, any Knock Out): it goes off
with Lucky Egg and the other Knock Out effects and Gastly's owner orders
them (official Q&A).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, def_for


def _is_haunter(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Haunter"


def _swelling_spite_applies(ctx) -> bool:
    return ctx.bench_space() > 0 and bool(ctx.deck())


async def swelling_spite(ctx):
    """Up to 2 Haunter from the deck onto the Bench, then shuffle."""
    if not ctx.deck():
        return
    picks = await ctx.search_deck(
        _is_haunter, count=min(2, ctx.bench_space()), minimum=0,
        prompt="Choose up to 2 Haunter to put onto your Bench")
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="9b229419-823b-5998-816f-ac6e16c0c957",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=92,
    abilities=[
        Ability(
            title="Swelling Spite",
            game_text="When this Pokémon is Knocked Out, search your deck for up to 2 Haunter and put them onto your Bench. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=swelling_spite,
            trigger_applies=_swelling_spite_applies,
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
