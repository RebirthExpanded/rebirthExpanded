"""Vivillon (JP M6a 005/103 -- 30th Celebrations).

Stage 2 Grass Pokemon, evolves from Spewpa. HP 120, weakness Fire x2,
retreat 1, regulation mark J.

  Ability  Guiding Dance  Once during your turn, flip a coin. If heads,
                          search your deck for a Pokemon, reveal it, and put
                          it into your hand. Then, shuffle your deck.
  Poison Powder  [GC] 60  Your opponent's Active Pokemon is now Poisoned.

The coin is flipped as part of using the Ability, so a tails spends the
turn's use and finds nothing.

The English 30th Celebrations release is not out, so the Japanese collector
number stands, as it does for the rest of the pool's M6a cards.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_pokemon_card


async def guiding_dance(ctx):
    """Heads: a Pokemon out of the deck and into your hand."""
    heads = (await ctx.flip_coins(1, "Guiding Dance"))[0]
    if not heads:
        return
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ee7dc8b0-f9b9-5c71-ba6e-544ee10db1b3",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Guiding Dance",
            game_text="Once during your turn, flip a coin. If heads, search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=guiding_dance,
        ),
        Attack(
            title="Poison Powder",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
