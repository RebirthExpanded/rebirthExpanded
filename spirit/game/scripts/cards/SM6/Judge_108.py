from spirit.game.data_utils import SupporterCardDef
from spirit.game.card_effects.support_common import requires_any_deck
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import judge


card = SupporterCardDef(
    guid="844bb265-b3fe-51da-a98b-c43786c85389",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter", "Judge"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="SM6",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=judge,
    # Neither player can shuffle, so nothing after it happens either.
    condition=requires_any_deck(),
)
