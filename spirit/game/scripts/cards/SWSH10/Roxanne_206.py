from spirit.game.card_effects.trainers import opponent_prizes_low, roxanne
from spirit.game.card_effects.support_common import all_of, requires_any_deck
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f6702dfe-3e6b-539c-981f-6a658ca56255",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxanne.Name",
    display_name="Roxanne",
    searchable_by=["Roxanne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=206,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=roxanne,
    # Neither player able to shuffle means nothing after it happens.
    condition=all_of(opponent_prizes_low, requires_any_deck())
)
