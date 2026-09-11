"""Luxurious Cape (SV - Paradox Rift 166/182 -- JP SV3a 055/062).

Pokemon Tool.  "If the Pokemon this card is attached to doesn't have a
Rule Box, it gets +100 HP, and if it is Knocked Out by damage from an
attack from your opponent's Pokemon, that player takes 1 more Prize card."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, has_rule_box
from spirit.game.session.passives import Passive, carrier_pokemon


class LuxuriousCapePassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon or has_rule_box(pokemon.archetype_id):
            return 0
        return 100

    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon or has_rule_box(pokemon.archetype_id):
            return 0
        if not ctx.is_attack_effect() or pokemon.entity_id not in ctx.attack_damage:
            return 0
        if ctx.attacker is None or ctx.attacker.owning_player_id == pokemon.owning_player_id:
            return 0
        return 1


card = PokemonToolCardDef(
    guid="ae4e4eac-2e49-50f6-8f4a-fbdd9794910f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuriousCape.Name",
    display_name="Luxurious Cape",
    searchable_by=["Luxurious Cape", "Pokémon Tool", "LuxuriousCape"],
    subtypes=["Pokémon Tool"],
    collector_number=166,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    passive=LuxuriousCapePassive(),
)
