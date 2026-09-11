"""Shrine of Memories (XY - Primal Clash 139/160 -- JP XY5-Bt 068/070).

Stadium.

  "Each player's evolved Pokemon can use any attack from its previous
   Evolutions. (That player still needs the necessary Energy to use each
   attack.)"

Memory Capsule for every evolved Pokemon on both sides while it stands.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Attack, StadiumCardDef, def_for
from spirit.game.models.board import PokemonEntity
from spirit.game.session.passives import Passive


class ShrineOfMemoriesPassive(Passive):
    def granted_attacks(self, board, pokemon, carrier):
        attacks = []
        for child in pokemon.children:
            if not isinstance(child, PokemonEntity):
                continue
            for ability in getattr(def_for(child.archetype_id), "abilities", None) or []:
                if isinstance(ability, Attack):
                    attacks.append(ability)
        return attacks


card = StadiumCardDef(
    guid="2f441976-bad0-5635-ba17-f5a277104aa4",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofMemories.Name",
    display_name="Shrine of Memories",
    searchable_by=["Shrine of Memories", "Stadium", "ShrineofMemories"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=ShrineOfMemoriesPassive(),
)
