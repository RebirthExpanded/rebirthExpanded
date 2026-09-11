"""Ancient Booster Energy Capsule (SV - Temporal Forces 140/162 -- JP SV5K
065/071).

Pokemon Tool.  "The Ancient Pokemon this card is attached to gets +60 HP,
recovers from all Special Conditions, and can't be affected by any
Special Conditions."

The +60 and the immunity are continuous passives; "recovers from all
Special Conditions" is the Tool on_attach hook (the same shape Therapeutic
Energy uses), run when the capsule is attached from hand to an Ancient
Pokemon.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _ancient(pokemon) -> bool:
    return "Ancient" in subtypes_for(pokemon.archetype_id)


async def ancient_booster_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is not None and _ancient(pokemon):
        await ctx.cure_all_conditions(pokemon)


class AncientBoosterPassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        return 60 if holder is pokemon and _ancient(holder) else 0

    def blocks_special_conditions(self, target, condition, carrier):
        holder = carrier_pokemon(carrier)
        return holder is target and _ancient(holder)


card = PokemonToolCardDef(
    guid="f32a8152-1da5-5980-8955-eb4309d81f2a",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientBoosterEnergyCapsule.Name",
    display_name="Ancient Booster Energy Capsule",
    searchable_by=["Ancient Booster Energy Capsule", "Pokémon Tool", "AncientBoosterEnergyCapsule"],
    subtypes=["Pokémon Tool"],
    collector_number=140,
    set_code="SV05",
    rarity=Rarities.Uncommon,
    regulation_mark="H",
    passive=AncientBoosterPassive(),
    on_attach=ancient_booster_on_attach,
)
