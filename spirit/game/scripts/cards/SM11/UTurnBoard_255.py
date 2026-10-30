"""U-Turn Board (SM - Unified Minds 211/236 -- JP SM10b 052/054).

Pokemon Tool.

  "The Retreat Cost of the Pokemon this card is attached to is [C] less. If
   this card is discarded from play, put it into your hand instead of the
   discard pile."

The second clause is a new destination hook: a card leaving PLAY may name
where it goes instead of the discard pile. Both discard paths ask -- the
effect layer's discard_cards (Tool Scrapper, Professor Turo's Scenario, an
attack that discards attached cards) and the knockout that takes the whole
stack down with the holder, which now decides every destination BEFORE it
moves anything, since the first move would take this card's own passive off
the board.

FROM PLAY is the whole clause: a copy discarded out of your hand for Ultra
Ball, or milled off the deck, goes to the discard pile like anything else.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import UTurnBoardPassive
from spirit.game.data_utils import PokemonToolCardDef

card = PokemonToolCardDef(
    guid='8fdf4d41-7ae5-509e-80f3-d5ff1c04528c',
    key='SM11',
    name="com.direwolfdigital.cake.data.archetypes.trainer.UTurnBoard.Name",
    display_name="U-Turn Board",
    searchable_by=["U-Turn Board", "Pokémon Tool", "UTurnBoard"],
    subtypes=["Pokémon Tool"],
    collector_number=255,
    set_code='SM11',
    rarity=Rarities.RareSecret,
    passive=UTurnBoardPassive(),
)
