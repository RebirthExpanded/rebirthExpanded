"""Passho Berry (SV08 184 -- JP SV7a 058; English SSP/184). Japanese art.
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
    guid="ab70f982-1aa3-5d19-8644-b4a9abcbdbee",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PasshoBerry.Name",
    display_name="Passho Berry",
    searchable_by=["Passho Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=184,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=_BerryPassive(PokemonTypes.WATER),
)
