from spirit.game.card_effects.trainers import switch, player_has_bench
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3a844764-8c54-5957-b576-875930501126",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=147,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=switch,
    condition=player_has_bench,
)
