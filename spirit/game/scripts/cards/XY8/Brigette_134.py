"""Brigette (XY - BREAKthrough 134/162 -- JP XY8-Bb 056/059).

Supporter.

  "Search your deck for 1 Basic Pokémon-EX or 3 Basic Pokémon (except for Pokémon-EX) and put them onto your Bench. Shuffle your deck afterward."

The mode is chosen first, then the search is capped by the Bench space
left. "Pokemon-EX" is the uppercase XY-era rule box: a Scarlet & Violet
ex counts as a plain Basic here.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.card_effects.trainers import brigette
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="58c4ab6a-af66-5e04-a6bb-ca1ee46cd5f5",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name",
    display_name="Brigette",
    searchable_by=["Brigette", "Supporter", "Brigette"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=brigette,
    condition=requires_bench_space(1),
)
