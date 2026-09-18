"""Magneton (SM - Cosmic Eclipse 69/236 -- JP SM11b 024/049).

Stage 1 Lightning Pokemon, evolves from Magnemite. HP 80, weakness
Fighting x2, resistance Metal -20, retreat 2.

  Ability  Call Signal  Once during your turn (before your attack), you may
                        search your deck for up to 3 Supporter cards, reveal
                        them, and put them into your hand. Then, shuffle
                        your deck. If you searched your deck in this way,
                        this Pokemon is Knocked Out.
  Magnetic Blast  [LLC] 50

Electrode's Buzzap Generator with Supporters instead of Energy: the
knockout is the price, so the opponent takes a Prize for it, and it is
paid whether or not the search found anything -- "if you searched" is
the act, not the result.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_supporter_card


async def call_signal(ctx):
    """Up to 3 Supporters out of the deck; then this Pokemon faints."""
    if not await ctx.ask_yes_no(
            "Search your deck for up to 3 Supporter cards? "
            "This Pokémon will be Knocked Out."):
        return
    picks = await ctx.search_deck(
        is_supporter_card, count=3, minimum=0,
        prompt="Choose up to 3 Supporter cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()
    await ctx.knock_out(ctx.source)


card = PokemonCardDef(
    guid="25785690-da35-5539-8f84-eb5332a1d820",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Call Signal",
            game_text="Once during your turn (before your attack), you may search your deck for up to 3 Supporter cards, reveal them, and put them into your hand. Then, shuffle your deck. If you searched your deck in this way, this Pokémon is Knocked Out.",
            activation=Activations.ONCE_PER_TURN,
            effect=call_signal,
            self_knockout=True,
        ),
        Attack(
            title="Magnetic Blast",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
