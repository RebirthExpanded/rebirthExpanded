"""Hall of Fame Belt (殿堂ベルト -- JP BW-P, Battle Carnival 2012 Spring
prize, numbered 153/BW-P; no English print).

Pokemon Tool.

  "As long as the Pokemon this card is attached to is your Active Pokemon,
   you draw 2 cards at the beginning of your turn instead of 1."

Rides the turn_draw_count hook: the holder must be its owner's Active
when the turn begins. A deck with only 1 card left still draws that one
(drawing nothing is the deck-out, drawing short is not).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class HallOfFameBeltPassive(Passive):
    def turn_draw_count(self, player_id, count, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder.owning_player_id != player_id \
                or not is_in_active_spot(holder):
            return count
        return max(count, 2)


card = PokemonToolCardDef(
    guid="35efd04e-c45c-5663-8ab8-871f17ced1f0",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HallofFameBelt.Name",
    display_name="Hall of Fame Belt",
    searchable_by=["Hall of Fame Belt", "Pokémon Tool", "HallofFameBelt"],
    subtypes=["Pokémon Tool"],
    collector_number=153,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    passive=HallOfFameBeltPassive(),
)
