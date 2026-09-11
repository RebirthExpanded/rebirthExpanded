"""Roxie (SM - Cosmic Eclipse 205/236 -- JP SM11b 054/049).

Supporter.

  "Discard up to 2 Pokemon that aren't Pokemon-GX or Pokemon-EX from your
   hand. Draw 3 cards for each card you discarded in this way."

The discard is the price and the draw is the payoff, but the cards thrown
away get their own say: Koffing and Weezing (CEC 76/77) name this Supporter
by name, so Roxie fires their window itself, after drawing -- which is what
"(Place damage counters after the effect of Roxie.)" asks for.

"Pokemon-GX or Pokemon-EX" is the SM/XY-era uppercase pair, so a Scarlet &
Violet Pokemon ex may be discarded, the same reading Mewtwo & Mew-GX's
Perfection takes from the other side.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import roxie, roxie_condition
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="bf13f09f-d922-5911-81ff-7afd053eafa3",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxie.Name",
    display_name="Roxie",
    searchable_by=["Roxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=roxie,
    condition=roxie_condition,
)
