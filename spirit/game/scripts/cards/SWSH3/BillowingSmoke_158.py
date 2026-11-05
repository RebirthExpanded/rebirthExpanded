from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon, ko_by_opposing_attack_damage


class BillowingSmokePassive(Passive):
    def prize_destination(self, pokemon, ctx, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return None
        if not ko_by_opposing_attack_damage(ctx, pokemon):
            return None
        return "discard"


card = PokemonToolCardDef(
    guid="2508ef44-0afb-5957-8126-b92f2a37fd1e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillowingSmoke.Name",
    display_name="Billowing Smoke",
    searchable_by=["Billowing Smoke", "Pokémon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=158,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    passive=BillowingSmokePassive()
)
