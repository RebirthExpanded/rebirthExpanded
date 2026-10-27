"""Ange Floette (ME4 75 -- JP M4 079; English CRI/75). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for



class AngeFloettePassive(Passive):
    """Each Mega Floette ex in play gets +150 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        return 150 if getattr(def_for(pokemon.archetype_id), "display_name", None) == "Mega Floette ex" else 0


card = StadiumCardDef(
    guid="3552d6eb-4576-5006-ad6b-4ff3230034b1",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AngeFloette.Name",
    display_name="Ange Floette",
    searchable_by=["Ange Floette", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=AngeFloettePassive(),
)
card.replaces_stadium = "Prism Tower"
