"""Focus Sash (XY - Furious Fists 91/111 -- JP XY3 084/096).

Pokemon Tool.

  "If the [F] Pokemon this card is attached to has full HP and would be
   Knocked Out by damage from an opponent's attack, that Pokemon is not
   Knocked Out and its remaining HP becomes 10 instead. Then, discard this
   card."

Sturdy on a string: the KO-survive interceptor with no flip and the
full-HP gate, answering only for a Fighting holder, and the sash goes to
the discard pile the moment it has done its job.
"""

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import GutsSurvivePassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import carrier_pokemon


def _is_fighting(pokemon) -> bool:
    return PokemonTypes.FIGHTING.value in (
        pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


class FocusSashPassive(GutsSurvivePassive):
    def __init__(self):
        super().__init__(hp_floor=10, title="Focus Sash", flip=False,
                         require_full_hp=True)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not _is_fighting(holder):
            return None
        amount = await super().damage_interceptor(ctx, calc, target, carrier)
        if amount is not None:
            await ctx.discard_cards([carrier])
        return amount


card = PokemonToolCardDef(
    guid="bf0dd342-c9be-53a8-b644-a9f02cf3928f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusSash.Name",
    display_name="Focus Sash",
    searchable_by=["Focus Sash", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=FocusSashPassive(),
)
