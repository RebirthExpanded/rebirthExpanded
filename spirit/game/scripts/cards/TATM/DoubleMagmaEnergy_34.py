"""Double Magma Energy (XY - Double Crisis 34/34).

Special Energy.

  "This card can only be attached to Team Magma's Pokemon. Discard this card
   at the end of the turn you attached it."
  "This card provides [F][F] Energy only while it is attached to a Team
   Magma's Pokemon."
  "(If this card is attached to anything other than a Team Magma's Pokemon,
   discard this card.)"

Triple Acceleration Energy's shape: attach_to refuses anything else,
discard_if_invalid covers an effect parking it elsewhere, so the flat
provides only ever applies on a Team Magma's Pokemon; the end-of-turn
discard rides the holder.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import discard_self_at_end_of_turn
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for


def _is_team_magma(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Team Magma's ")


card = EnergyCardDef(
    guid="cf3d6a67-253e-5727-b284-ce8ba6540fb8",
    key="TATM",
    name="Double Magma Energy",
    display_name="Double Magma Energy",
    searchable_by=["Double Magma Energy", "Special", "DoubleMagmaEnergy"],
    subtypes=["Special"],
    collector_number=34,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=_is_team_magma,
    discard_if_invalid=True,
    provides=[[PokemonTypes.FIGHTING, PokemonTypes.FIGHTING]],
    granted_abilities=[
        Ability(
            title="Double Magma Energy",
            game_text="Discard this card at the end of the turn you attached it.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_at_end_of_turn("Double Magma Energy"),
        ),
    ],
)
