"""Survival Brace (SV - Twilight Masquerade 164/167 -- JP SV5a).

Pokemon Tool, ACE SPEC.

  "If the Pokemon this card is attached to has full HP and would be
   Knocked Out by damage from an attack from your opponent's Pokemon, it is
   not Knocked Out, and its remaining HP becomes 10. Then, discard this
   card."

Focus Sash without the type gate.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import GutsSurvivePassive
from spirit.game.data_utils import PokemonToolCardDef



class SurvivalBracePassive(GutsSurvivePassive):
    def __init__(self):
        super().__init__(hp_floor=10, title="Survival Brace", flip=False,
                         require_full_hp=True)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        amount = await super().damage_interceptor(ctx, calc, target, carrier)
        if amount is not None:
            await ctx.discard_cards([carrier])
        return amount


card = PokemonToolCardDef(
    guid="7226024d-5204-585b-99d0-acbca5ce2e9b",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurvivalBrace.Name",
    display_name="Survival Brace",
    searchable_by=['Survival Brace', 'Item', 'Pokémon Tool', 'ACE SPEC', 'SurvivalBrace'],
    subtypes=['Item', 'Pokémon Tool', 'ACE SPEC'],
    collector_number=164,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    passive=SurvivalBracePassive(),
)
