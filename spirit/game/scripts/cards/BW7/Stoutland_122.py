"""Stoutland (BW - Boundaries Crossed 122/149).

Stage 2 Colorless Pokemon. HP 140, weakness Fighting x2, no resistance,
retreat 3.

  Ability  Sentinel  As long as this Pokemon is your Active Pokemon, your
                     opponent can't play any Supporter cards from his or
                     her hand.

  Wild Tackle [CCC] 90  Flip a coin. If tails, this Pokemon does 20 damage
                        to itself.

A Supporter lock where Vileplume's is an Item lock, and the same shape:
a blocks_trainer_play passive, so it is recomputed from the board and an
ability lock switches it off. Two conditions, both printed: this Pokemon
must be Active, and only the OPPONENT is stopped -- your own Supporter
still plays.

The self-damage is flip_damage's tails_self_damage, which lands after the
printed 90 and skips the attacker's own damage modifiers.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, TrainerType
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class SentinelPassive(Passive):
    """While this Pokemon is Active, the opponent can play no Supporters."""

    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(carrier):
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value


card = PokemonCardDef(
    guid="2cdb6b7f-eaae-5349-b223-40778beefc05",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=122,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Ability(
            title="Sentinel",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Supporter cards from his or her hand.",
            passive=SentinelPassive(),
        ),
        Attack(
            title="Wild Tackle",
            game_text="Flip a coin. If tails, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=flip_damage(coins=1, tails_self_damage=20),
        ),
    ],
)
