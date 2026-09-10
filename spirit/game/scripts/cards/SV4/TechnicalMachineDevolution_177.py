"""Technical Machine: Devolution (SV - Paradox Rift 177/182 --
JP SV4K 063/066).

Pokemon Tool.

  "The Pokemon this card is attached to can use the attack on this card.
   (You still need the necessary Energy to use this attack.) If this card
   is attached to 1 of your Pokemon, discard it at the end of your turn."

  Devolution [C]  Devolve each of your opponent's evolved Pokemon and put
                  the highest Stage Evolution card on each of them into
                  your opponent's hand.

The third Technical Machine in the pool and the same two granted
abilities: the Attack the holder borrows and the END_OF_TURN Ability that
burns the Tool off.

Where the Sprays take one Pokemon of YOURS, this takes one step off EVERY
evolved Pokemon of THEIRS, Active and Bench alike, and the cards go to
their hand. Each remaining stage keeps its damage, which is what makes
this a knockout tool rather than a tempo one -- and each is stamped
devolved-this-turn, so nothing re-evolves before their next turn.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import devolvable
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn
from spirit.game.data_utils import (Ability, Attack, PokemonToolCardDef,
                                    Triggers)

TM_DEVOLUTION = "Technical Machine: Devolution"


async def devolution(ctx):
    """One step off every evolved Pokemon they have."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        if not devolvable(pokemon) or ctx.effects_blocked(pokemon):
            continue
        await ctx.devolve_pokemon(pokemon, steps=1, destination="hand")


card = PokemonToolCardDef(
    granted_abilities=[
        Attack(
            title="Devolution",
            game_text="Devolve each of your opponent's evolved Pokémon and put the highest Stage Evolution card on each of them into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=devolution,
        ),
        Ability(
            title=TM_DEVOLUTION,
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_tool_at_end_of_turn(TM_DEVOLUTION),
        ),
    ],
    guid="446a3f29-1de4-5c0b-853f-99e222912ff4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineDevolution.Name",
    display_name=TM_DEVOLUTION,
    searchable_by=["Technical Machine: Devolution", "Item", "Pokémon Tool",
                   "TechnicalMachineDevolution"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=177,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
)
