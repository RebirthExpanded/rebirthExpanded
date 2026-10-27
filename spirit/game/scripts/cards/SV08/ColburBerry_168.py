"""Colbur Berry (SV08 168 -- JP SV8 099; English SSP/168). Japanese art.
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
    guid="c8ad466e-bedd-50ba-9656-c1e2af969ac9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColburBerry.Name",
    display_name="Colbur Berry",
    searchable_by=["Colbur Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=168,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=_BerryPassive(PokemonTypes.DARKNESS),
)
