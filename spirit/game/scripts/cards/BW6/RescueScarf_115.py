from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon, ko_by_opposing_attack_damage


class RescueScarfPassive(Passive):
    """If the holder is Knocked Out by damage from an opponent's attack, the
    Pok\u00e9mon (and its pre-evolutions) go to hand; attachments still go to
    the discard pile (the engine routes non-Pok\u00e9mon cards there)."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        # Evaluated pre-move with the KO ctx: remember KOs by attack DAMAGE
        # only -- damage counters or a direct Knock Out from an attack don't.
        if carrier_pokemon(carrier) is pokemon:
            pokemon._rescue_scarf_ko = ko_by_opposing_attack_damage(ctx, pokemon)
        return count

    def knockout_destination(self, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon and getattr(pokemon, "_rescue_scarf_ko", False):
            pokemon._rescue_scarf_ko = False
            return "hand"
        return None


card = PokemonToolCardDef(
    guid="194759b5-60eb-5d11-96f9-7554d94329a1",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueScarf.Name",
    display_name="Rescue Scarf",
    searchable_by=["Rescue Scarf", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=115,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    passive=RescueScarfPassive()
)
