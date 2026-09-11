"""Jacq (SV - Scarlet & Violet 175/198 -- JP SV1S 074/078, the art here).

Supporter.

  "Search your deck for up to 2 Evolution Pokemon, reveal them, and put
   them into your hand. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck, search_to_hand
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_evolution_pokemon

card = SupporterCardDef(
    guid="48b06b5e-9b4a-5e1c-83eb-3fc97fb9a61c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacq.Name",
    display_name="Jacq",
    searchable_by=["Jacq", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=search_to_hand(is_evolution_pokemon, count=2, minimum=0, reveal=True,
                          prompt="Choose up to 2 Evolution Pokémon to put into your hand."),
)
