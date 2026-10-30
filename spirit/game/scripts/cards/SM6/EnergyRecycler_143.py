from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import energy_recycler, has_basic_energy_in_discard


card = ItemCardDef(
    guid="522c6d24-1020-5d70-951e-41ae92eaf0d0",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item", "EnergyRecycler"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SM6",
    regulation_mark="I",
    rarity=Rarities.RareSecret,
    condition=has_basic_energy_in_discard,
    effect=energy_recycler,
)
