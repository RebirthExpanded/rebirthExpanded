from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import energy_recycler, has_basic_energy_in_discard


card = ItemCardDef(
    guid="3ba4e70b-c3b0-5a11-99e0-f797d657a7bd",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item", "EnergyRecycler"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=has_basic_energy_in_discard,
    effect=energy_recycler,
)
