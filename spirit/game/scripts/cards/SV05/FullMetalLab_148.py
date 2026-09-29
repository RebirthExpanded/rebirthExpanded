"""Full Metal Lab (SV - Temporal Forces 148/162 -- JP SV5M 070/071).

Stadium.

  "[M] Pokemon (both yours and your opponent's) take 30 less damage from
   attacks from the opponent's Pokemon (after applying Weakness and
   Resistance)."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import Passive


class FullMetalLabPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.target is None:
            return
        if is_pokemon_of_type(calc.target, PokemonTypes.METAL):
            calc.amount = max(0, calc.amount - 30)


card = StadiumCardDef(
    guid="c2407de6-bacb-5c7f-b1d0-56aa6a88a0fb",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullMetalLab.Name",
    display_name="Full Metal Lab",
    searchable_by=["Full Metal Lab", "Stadium", "FullMetalLab"],
    subtypes=["Stadium"],
    collector_number=148,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=FullMetalLabPassive(),
)
