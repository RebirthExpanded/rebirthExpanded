"""Thick Scale (ME - Ascended Heroes 211 -- JP M2a 164).

Pokemon Tool.

  "The [N] Pokemon this card is attached to takes 50 less damage from
   attacks from your opponent's [G], [R], [W], or [L] Pokemon (after
   applying Weakness and Resistance)."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.effects import live_pokemon_types
from spirit.game.session.passives import Passive, carrier_pokemon

_ATTACKER_TYPES = {t.value for t in (PokemonTypes.GRASS, PokemonTypes.FIRE,
                                     PokemonTypes.WATER, PokemonTypes.LIGHTNING)}


class ThickScalePassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is None:
            return
        target = calc.target
        if carrier_pokemon(carrier) is not target:
            return
        if PokemonTypes.DRAGON.value not in live_pokemon_types(target):
            return
        if _ATTACKER_TYPES & set(live_pokemon_types(calc.attacker)):
            calc.amount = max(0, calc.amount - 50)


card = PokemonToolCardDef(
    guid="064b9dbf-cbae-5578-9939-628e589c7ab2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThickScale.Name",
    display_name="Thick Scale",
    searchable_by=["Thick Scale", "Pokémon Tool", "Tool", "ThickScale"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=211,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=ThickScalePassive(),
)
