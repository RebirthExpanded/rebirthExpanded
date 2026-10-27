"""Haban Berry (SV085 111 -- JP SV8a 156; English PRE/111). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.attributes import PokemonTypes


class _BerryPassive(Passive):
    """Damaged by an opposing <type> Pokemon's attack: 60 less (after W/R),
    then discard this card."""

    def __init__(self, ptype):
        self.ptype = ptype

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and target is holder and calc.amount > 0 and attacker is not None):
            return None
        if self.ptype.value not in (attacker.get_attribute(AttrID.POKEMON_TYPES) or []):
            return None
        await ctx.discard_cards([carrier])
        return max(0, calc.amount - 60)
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


card = PokemonToolCardDef(
    guid="5c46c243-d5af-51a8-8fca-7608cf957530",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HabanBerry.Name",
    display_name="Haban Berry",
    searchable_by=["Haban Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=111,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    passive=_BerryPassive(PokemonTypes.DRAGON),
)
