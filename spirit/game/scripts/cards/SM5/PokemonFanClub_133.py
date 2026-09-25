"""Pokemon Fan Club (SM - Ultra Prism 133/156 -- JP SM5S 061/066).

Supporter.

  "Search your deck for up to 2 Basic Pokemon, reveal them, and put them
   into your hand. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import is_basic, search_to_hand
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="953ca7aa-987e-5052-a277-3f94e172721b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter", "PokemonFanClub"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic, count=2, reveal=True,
                          prompt="Choose up to 2 Basic Pokémon."),
)
