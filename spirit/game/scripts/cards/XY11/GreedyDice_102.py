"""Greedy Dice (XY - Steam Siege 102/114).

Item.

  "You can play this card only if you took it as a face-down Prize card,
   before you put it into your hand."
  "Flip a coin. If heads, take 1 more Prize card."

Jirachi {*}'s Item cousin, and mechanically Dream Ball's twin: the card is
never playable from hand, and its whole life is the ON_TAKEN_AS_PRIZE
window that _take_prizes opens while it is still a Prize card. The
condition returns a flat False so the deck builder and the hand offers
both leave it alone; the window is the only way in.

Where Jirachi {*} takes its extra Prize outright, this one flips for it,
which is the only real difference between them. The flip lives in the
card's own effect rather than the window, so the sequence reads the way
the card does: accept the window -> the Item is played -> the coin
decides. That also means the flip goes through _execute_play_trainer, so
a coin-rerolling effect sees it like any other Item's flip, and the card
lands in the discard afterwards on the normal Trainer path.

Face-down only, and before it reaches hand, both come free from the
window itself -- see Jirachi {*} for why the timing matters (in hand,
Garbotoxin would silence it).
"""

from spirit.game.data_utils import ItemCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    greedy_dice, greedy_dice_playable, greedy_dice_prize_window,
)

card = ItemCardDef(
    guid="648dacce-e658-5a62-8070-3236c9551900",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreedyDice.Name",
    display_name="Greedy Dice",
    searchable_by=["Greedy Dice", "Item", "GreedyDice"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    effect=greedy_dice,
    condition=greedy_dice_playable,
    abilities=[
        Ability(
            title="Greedy Dice",
            game_text="You can play this card only if you took it as a face-down Prize card, before you put it into your hand.",
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=greedy_dice_prize_window,
        ),
    ],
)
