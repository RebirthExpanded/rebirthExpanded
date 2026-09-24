"""Technical Machine: Evolution (SV - Paradox Rift 178/182).

Pokemon Tool.

  "The Pokemon this card is attached to can use the attack on this card.
   (You still need the necessary Energy to use this attack.) If this card
   is attached to 1 of your Pokemon, discard it at the end of your turn."

  Evolution [C]  Choose up to 2 of your Benched Pokemon. For each of those
                 Pokemon, search your deck for a card that evolves from
                 that Pokemon and put it onto that Pokemon to evolve it.
                 Then, shuffle your deck.

Earthen Seal Stone's shape: a Tool whose granted_abilities carry an
Attack, so the holder gains it while the Tool is attached. The difference
is the second sentence -- this one burns off at end of turn, which is a
granted Ability on an END_OF_TURN trigger, the same idea as Ignition and
Triple Acceleration Energy but walking the holder's Tool stack instead of
its Energy.

The evolution itself is Pokemon Breeder's Nurturing narrowed to the Bench:
"a card that evolves from that Pokemon" is the DIRECT pre-evolution, so it
matches EVOLUTION_LOGIC_FROM against the target's own name rather than the
whole-line evolves_from() that Rare Candy needs to skip a stage.

The ordinary evolution timing does NOT apply. This is an attack putting
the card onto the Pokemon, not the player taking their evolve action, so
a Pokemon benched this turn is a legal target and so is one on the first
turn. ctx.evolve_pokemon already bypasses those rules on its own -- the
cards that DO enforce them (Rare Candy, Pokemon Breeder's Nurturing) do it
by filtering their own candidate list with may_evolve_target, and this one
deliberately does not.

Unlike Wally and Boost Shake, which are unplayable with nothing to evolve,
this is an attack: it can always be declared. What it cannot do is open the
deck for a search that has no target, so with no evolvable Pokemon on the
Bench it simply does nothing.

The pool's first Paradox Rift card, so SV4 is registered here.
"""

from spirit.game.card_effects.support_common import evolves_from, pokemon_can_still_evolve
from spirit.game.data_utils import (Attack, Ability, PokemonToolCardDef,
                                    Triggers, has_evolution)
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn

TM_EVOLUTION = "Technical Machine: Evolution"
MAX_TARGETS = 2


def _evolvable_bench(ctx):
    """Every Benched Pokemon a card in the pool evolves from. No
    may_evolve_target filter: see the note above on timing."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    return [p for p in (bench.children if bench else [])
            if pokemon_can_still_evolve(ctx.board, ctx.player_id, p)]


def _evolution_condition(board, player_id, pokemon) -> bool:
    """Usable only with a Benched Pokemon whose evolution can still come out
    of the deck (not every copy of it in the discard pile)."""
    bench = board.find_player_area(player_id, "bench")
    return any(pokemon_can_still_evolve(board, player_id, p)
               for p in (bench.children if bench else []))


async def evolution(ctx):
    """Evolve up to 2 of your Benched Pokemon straight out of the deck."""
    candidates = _evolvable_bench(ctx)
    if not candidates:
        return
    targets = await ctx.choose_cards(
        candidates, MAX_TARGETS, minimum=0,
        prompt="Choose up to 2 of your Benched Pokémon to evolve.",
    )
    if not targets:
        return
    for target in targets:
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        picks = await ctx.search_deck(
            lambda c, name=logic_name: (
                evolves_from(c, name)),
            count=1, minimum=0,
            prompt="Choose a card that evolves from that Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    granted_abilities=[
        Attack(
            title="Evolution",
            game_text="Choose up to 2 of your Benched Pokémon. For each of those Pokémon, search your deck for a card that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_evolution_condition,
            effect=evolution,
        ),
        Ability(
            title=TM_EVOLUTION,
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_tool_at_end_of_turn(TM_EVOLUTION),
        ),
    ],
    guid="a2868773-689d-5240-8338-3ed47dee6f79",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineEvolution.Name",
    display_name=TM_EVOLUTION,
    searchable_by=["Technical Machine: Evolution", "Item", "Pokémon Tool",
                   "TechnicalMachineEvolution"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=178,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
)
