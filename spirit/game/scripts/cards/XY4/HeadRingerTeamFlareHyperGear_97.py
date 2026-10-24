"""Head Ringer Team Flare Hyper Gear (XY - Phantom Forces 97/119).

Pokemon Tool (Team Flare Hyper Gear).

  "Attach this Pokemon Tool to 1 of your opponent's Pokemon-EX that
   doesn't already have a Pokemon Tool attached to it."
  "The attacks of the Pokemon this card is attached to cost [C] more."
  "When this card is removed from a Pokemon for any reason, put this card
   in its owner's discard pile."

attach_to_opponent offers the opponent's Pokemon-EX as targets;
discard_when_removed (and the Knock Out routing) sends it to its owner's
discard pile however it leaves.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_pokemon_ex(pokemon) -> bool:
    return "EX" in (subtypes_for(pokemon.archetype_id) or [])


class HeadRingerPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon:
            cost = dict(cost)
            cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = PokemonToolCardDef(
    guid="dd0394e5-87bb-5405-b88c-f342f6c4b60e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeadRingerTeamFlareHyperGear.Name",
    display_name="Head Ringer Team Flare Hyper Gear",
    searchable_by=["Head Ringer Team Flare Hyper Gear", "Head Ringer", "Pokémon Tool", "Team Flare Hyper Gear"],
    subtypes=["Pokémon Tool", "Team Flare Hyper Gear"],
    collector_number=97,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    attach_to_opponent=True,
    discard_when_removed=True,
    attach_to=_is_pokemon_ex,
    passive=HeadRingerPassive(),
)
