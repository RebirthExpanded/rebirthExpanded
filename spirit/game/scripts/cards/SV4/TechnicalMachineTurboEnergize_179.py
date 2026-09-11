"""Technical Machine: Turbo Energize (SV - Paradox Rift 179/182 -- JP SV3a 056/062).

Pokemon Tool.

  "The Pokemon this card is attached to can use the attack on this card.
   (You still need the necessary Energy to use this attack.) If this card
   is attached to 1 of your Pokemon, discard it at the end of your turn."

  Turbo Energize [C]  Search your deck for up to 2 Basic Energy cards and
                      attach them to your Benched Pokemon in any way you
                      like. Then, shuffle your deck.

Technical Machine: Devolution's shape. Each found Energy picks its own
Benched Pokemon; with an empty Bench nothing is searched but the deck is
still shuffled.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn
from spirit.game.data_utils import (Ability, Attack, PokemonToolCardDef,
                                    Triggers)
from spirit.game.session.effects import is_basic_energy

TM_TURBO_ENERGIZE = "Technical Machine: Turbo Energize"


async def turbo_energize(ctx):
    bench = ctx.my_bench()
    if bench:
        picks = await ctx.search_deck(
            is_basic_energy, count=2, minimum=0,
            prompt="Choose up to 2 Basic Energy cards to attach to your Benched Pokémon.")
        for energy in picks:
            target = await ctx.choose_pokemon(
                ctx.my_bench(), "Choose a Benched Pokémon to attach the Energy to")
            if target is None:
                target = ctx.my_bench()[0]
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    granted_abilities=[
        Attack(
            title="Turbo Energize",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=turbo_energize,
        ),
        Ability(
            title=TM_TURBO_ENERGIZE,
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_tool_at_end_of_turn(TM_TURBO_ENERGIZE),
        ),
    ],
    guid="532caab2-13d5-5462-9fb5-72f6c107c7bd",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTurboEnergize.Name",
    display_name=TM_TURBO_ENERGIZE,
    searchable_by=["Technical Machine: Turbo Energize", "Item", "Pokémon Tool",
                   "TechnicalMachineTurboEnergize"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=179,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
)
