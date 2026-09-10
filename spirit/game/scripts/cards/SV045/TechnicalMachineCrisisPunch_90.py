"""Technical Machine: Crisis Punch (SV - Paldean Fates 90/91 -- JP SV4a 170/190).

Pokemon Tool.

  "The Pokemon this card is attached to can use the attack on this card.
   (You still need the necessary Energy to use this attack.) If this card
   is attached to 1 of your Pokemon, discard it at the end of your turn."

  Crisis Punch [CCC] 280  This attack can be used only if your opponent has
                          exactly 1 Prize card remaining.

Technical Machine: Evolution's twin, down to the end-of-turn burn-off, so
it is the same two granted abilities: the Attack the holder borrows and
the END_OF_TURN Ability that discards the Tool.

"Only if your opponent has exactly 1 Prize card remaining" is an attack
usage restriction, so it goes on the Attack's condition and is re-read
every time the panel is built -- taking their sixth Prize card mid-turn
turns the attack off again, and Redeemable Ticket re-laying a spread turns
it on or off with the new count. Exactly 1: two Prizes left is too early,
none left means the game is already over.

The pool's first Paldean Fates card, so SV045 is registered here.
"""

from spirit.game.data_utils import (Attack, Ability, PokemonToolCardDef,
                                    Triggers)
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.support_common import opponent_on_last_prize
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn

TM_CRISIS_PUNCH = "Technical Machine: Crisis Punch"


card = PokemonToolCardDef(
    granted_abilities=[
        Attack(
            title="Crisis Punch",
            game_text="This attack can be used only if your opponent has exactly 1 Prize card remaining.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=280,
            condition=opponent_on_last_prize,
        ),
        Ability(
            title=TM_CRISIS_PUNCH,
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_tool_at_end_of_turn(TM_CRISIS_PUNCH),
        ),
    ],
    guid="dc7009c2-469c-564d-9f04-cb576a12b843",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineCrisisPunch.Name",
    display_name=TM_CRISIS_PUNCH,
    searchable_by=["Technical Machine: Crisis Punch", "Item", "Pokémon Tool",
                   "TechnicalMachineCrisisPunch"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=90,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
)
