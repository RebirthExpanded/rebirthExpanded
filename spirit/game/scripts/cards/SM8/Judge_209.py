from spirit.game.data_utils import SupporterCardDef
from spirit.game.card_effects.support_common import requires_any_deck
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import judge


card = SupporterCardDef(
    guid="96ab001e-a1e2-51da-8492-0b80104abea5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter", "Judge"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SM8",
    regulation_mark="I",
    rarity=Rarities.RareUltra,
    effect=judge,
    # Neither player can shuffle, so nothing after it happens either.
    condition=requires_any_deck(),
)
