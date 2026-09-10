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

Nothing here waives the ordinary evolution timing -- unlike Wally, the
card says nothing about it -- so a Pokemon benched this turn is not a
legal target, and neither is anything on turn 1. That gating is
turn_state.may_evolve_target, the same check Rare Candy and Breeder's
Nurturing use.

The pool's first Paradox Rift card, so SV4 is registered here.
"""

from spirit.game.data_utils import Attack, Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn

TM_EVOLUTION = "Technical Machine: Evolution"
MAX_TARGETS = 2


def _evolvable_bench(ctx):
    turn_state = ctx.session.turn_state
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    return [p for p in (bench.children if bench else [])
            if turn_state.may_evolve_target(p.entity_id)]


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
                c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name),
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
