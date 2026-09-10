"""Triple Acceleration Energy (SM - Unbroken Bonds 190/214).

Special Energy.

  "This card can only be attached to Evolution Pokemon. If this card is
   attached to 1 of your Pokemon, discard it at the end of the turn."
  "This card provides [C][C][C] Energy only while it is attached to an
   Evolution Pokemon."
  "If this card is attached to anything other than an Evolution Pokemon,
   discard this card."

Ignition Energy's neighbour, and the difference is the whole card. Ignition
goes on anything and provides 1, with a passive raising it to 3 on an
Evolution. This one is RESTRICTED to Evolution Pokemon, so it needs no
passive at all: attach_to refuses the attach, discard_if_invalid handles
the sentence for when an effect parks it somewhere illegal anyway, and the
provides is a flat three. "Only while attached to an Evolution Pokemon" is
then already true of every board state the card can reach.

Both cards burn themselves off at end of turn, which is now
discard_self_at_end_of_turn: the trigger fires on the holder, so the effect
picks its own copies back out of what is attached, by printed name.

The secret print (SM10 234) is the same card and is not implemented here.
"""

from spirit.game.data_utils import EnergyCardDef, Ability, Triggers
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import discard_self_at_end_of_turn
from spirit.game.session.effects import is_evolution_pokemon

card = EnergyCardDef(
    guid="5c8088f8-340a-5329-851b-45acd1709d9e",
    key="SM10",
    name="Triple Acceleration Energy",
    display_name="Triple Acceleration Energy",
    searchable_by=["Triple Acceleration Energy", "Special",
                   "TripleAccelerationEnergy"],
    subtypes=["Special"],
    collector_number=190,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_evolution_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.COLORLESS,
               PokemonTypes.COLORLESS,
               PokemonTypes.COLORLESS]],
    granted_abilities=[
        Ability(
            title="Triple Acceleration Energy",
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of the turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_at_end_of_turn("Triple Acceleration Energy"),
        ),
    ],
)
