"""Protective Goggles (SV035 164 -- JP SV2a 157; English MEW/164). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_basic_pokemon_in_play
from spirit.game.session.passives import carrier_pokemon


class ProtectiveGogglesPassive(Passive):
    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if calc.target is holder and is_basic_pokemon_in_play(holder):
            calc.weakness_applies = False


card = PokemonToolCardDef(
    guid="1a4fbdd6-4be5-5a98-a984-1d22d1572a8a",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProtectiveGoggles.Name",
    display_name="Protective Goggles",
    searchable_by=["Protective Goggles", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=164,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=ProtectiveGogglesPassive(),
)
