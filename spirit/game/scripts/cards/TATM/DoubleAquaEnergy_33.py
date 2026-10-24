"""Double Aqua Energy (XY - Double Crisis 33/34).

Special Energy.

  "This card can only be attached to Team Aqua's Pokemon. Discard this card
   at the end of the turn you attached it."
  "This card provides [W][W] Energy only while it is attached to a Team
   Aqua's Pokemon."
  "(If this card is attached to anything other than a Team Aqua's Pokemon,
   discard this card.)"

Triple Acceleration Energy's shape: attach_to refuses anything else,
discard_if_invalid covers an effect parking it elsewhere, so the flat
provides only ever applies on a Team Aqua's Pokemon; the end-of-turn
discard rides the holder.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import discard_self_at_end_of_turn
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for


def _is_team_aqua(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Team Aqua's ")


card = EnergyCardDef(
    guid="483ce702-6169-5dbe-9e8d-8f08a8a1bf52",
    key="TATM",
    name="Double Aqua Energy",
    display_name="Double Aqua Energy",
    searchable_by=["Double Aqua Energy", "Special", "DoubleAquaEnergy"],
    subtypes=["Special"],
    collector_number=33,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=_is_team_aqua,
    discard_if_invalid=True,
    provides=[[PokemonTypes.WATER, PokemonTypes.WATER]],
    granted_abilities=[
        Ability(
            title="Double Aqua Energy",
            game_text="Discard this card at the end of the turn you attached it.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_at_end_of_turn("Double Aqua Energy"),
        ),
    ],
)
