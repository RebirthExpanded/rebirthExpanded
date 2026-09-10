"""Green's Exploration (SM - Unbroken Bonds 175/214 -- JP SM9b 048/054).

Supporter.

  "You can play this card only if you have no Pokemon with Abilities in
   play.

   Search your deck for up to 2 Trainer cards, reveal them, and put them
   into your hand. Then, shuffle your deck."

The restriction is the card's own playability gate, so it is a condition
rather than something checked mid-effect: with an Ability Pokemon on your
board the Supporter is simply not offered.

"Pokemon with Abilities" is the PRINTED Ability, the same reading Chimecho
and Froslass use -- an Ability switched off by Path to the Peak or a
Garbotoxin is still printed on the card, so it still locks this out.
Attacks are not Abilities, which is what has_printed_ability filters.

It finds any TRAINER, Items, Supporters and Stadiums alike -- including a
second Green's Exploration.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import has_printed_ability
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_trainer_card


def _no_ability_pokemon_in_play(board, player_id, card=None):
    return not any(has_printed_ability(p)
                   for p in board.pokemon_in_play(player_id))


card = SupporterCardDef(
    guid="7553e2a7-8cd0-5c3c-926b-268487877d44",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter", "GreensExploration"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_trainer_card, count=2, minimum=0,
        prompt="Choose up to 2 Trainer cards to put into your hand."),
    condition=_no_ability_pokemon_in_play,
)
