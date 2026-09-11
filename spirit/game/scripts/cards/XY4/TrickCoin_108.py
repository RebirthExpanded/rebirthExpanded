"""Trick Coin (XY - Phantom Forces 108/119 -- JP XY-P promo).

Pokemon Tool.

  "Once during your turn, after you flip any coins for an attack of the
   Pokemon this card is attached to, you may ignore all effects of those
   coin flips and begin flipping those coins again. (You may only use
   effects that let you flip coins again, including effects from other
   cards, once during your turn.)"

Backtrack Badge without the Colorless clause. The parenthetical is the
rule the whole re-flip family shares here: one re-flip per turn across
every source (this, Glimwood Tangle, Victini's Victory Star, Backtrack
Badge), tracked by the turn's single attack_coin_reroll_used flag. The
re-flip is only ever offered for coins flipped for an attack's effect --
a Confusion or Smokescreen check coin is not one of those and is never
re-flipped -- and a first coin fixed by Will is not fixed again on the
re-flip.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class TrickCoinPassive(Passive):
    def offers_attack_coin_reroll(self, player_id, carrier, attacker=None):
        holder = carrier_pokemon(carrier)
        if holder is None or holder.owning_player_id != player_id:
            return False
        return attacker is None or attacker is holder


card = PokemonToolCardDef(
    guid="a91d5490-6f1f-5fad-9efe-8ef79048371d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrickCoin.Name",
    display_name="Trick Coin",
    searchable_by=["Trick Coin", "Pokémon Tool", "TrickCoin"],
    subtypes=["Pokémon Tool"],
    collector_number=108,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=TrickCoinPassive(),
)
