"""Herdier (SM - Sun & Moon 104/149).

Stage 1 Colorless Pokemon. HP 90, weakness Fighting x2, no resistance,
retreat 1.

  Ability  Treasure Hunt  When you play this Pokemon from your hand to
                          evolve 1 of your Pokemon during your turn, you
                          may put an Item card from your discard pile into
                          your hand.

  Bite [CCC] 50

An ON_EVOLVE trigger with a "you may", so it asks first and then offers the
Item cards -- Hariyama's Heave-Ho Catcher shape. "An Item card" goes
through counts_as_item, the same question Lillipup's Pickup asks.
"""

from spirit.game.data_utils import (PokemonCardDef, Attack, Ability, Triggers,
                                    counts_as_item)
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def treasure_hunt(ctx):
    """On evolving into this: you may take an Item back from the discard."""
    items = [c for c in ctx.discard_pile() if counts_as_item(c.archetype_id)]
    if not items:
        return
    if not await ctx.ask_yes_no(
            "Put an Item card from your discard pile into your hand?"):
        return
    picks = await ctx.choose_cards(
        items, 1, prompt="Choose an Item card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="8d11214e-7d8c-59b1-b9d2-ac0dce5fe03c",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    display_name="Herdier",
    searchable_by=["Herdier", "Stage 1", "Herdier"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    family_id=506,
    abilities=[
        Ability(
            title="Treasure Hunt",
            game_text=(
                "When you play this Pokémon from your hand to evolve 1 of "
                "your Pokémon during your turn, you may put an Item card "
                "from your discard pile into your hand."
            ),
            trigger=Triggers.ON_EVOLVE,
            effect=treasure_hunt,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
