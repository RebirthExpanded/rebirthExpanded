"""Antique Helix Fossil (SV035 153 -- JP SV2a 154; English MEW/153). Japanese art.
Item (fossil).
  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."
  Ability  Helical Swell  As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand.
Antique Cover Fossil's shape: FossilItemCardDef with FossilBodyPassive
plus the discard Ability.
"""
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_stadium_card
from spirit.game.session.passives import Passive

class HelicalSwellPassive(Passive):
    """Active: the opponent can't play Stadium cards from their hand."""

    def blocks_trainer_play(self, card, player_id, carrier):
        return player_id != carrier.owning_player_id and is_stadium_card(card) and is_in_active_spot(carrier)


ABILITY_PASSIVE = HelicalSwellPassive()

card = FossilItemCardDef(
    guid="cdd4c405-00d6-5a85-908d-a3fff6482bff",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueHelixFossil.Name",
    display_name="Antique Helix Fossil",
    searchable_by=["Antique Helix Fossil", "Item", "AntiqueHelixFossil"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Helical Swell",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand.",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
