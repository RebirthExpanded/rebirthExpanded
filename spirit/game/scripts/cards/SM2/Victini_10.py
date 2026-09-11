"""Victini (SM - Guardians Rising 10/145 -- JP SM2K 006/050).

Basic Fire Pokemon. HP 70, weakness Water x2, retreat 1.

  Ability  Victory Star  Once during your turn, after you flip any coins
                         for an attack, you may ignore all results of those
                         coin flips and begin flipping those coins again.
                         You can't use more than 1 Victory Star Ability
                         each turn.
  V-Flame  [RC] 50

Glimwood Tangle as an Ability, for its owner's attacks only. It shares the
turn's one re-flip with every other re-flip source, which covers both the
card's own "not more than 1 Victory Star each turn" and the rule that only
one re-flip effect may be used at all.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class VictoryStarPassive(Passive):
    def offers_attack_coin_reroll(self, player_id, carrier, attacker=None):
        return carrier.owning_player_id == player_id


card = PokemonCardDef(
    guid="5a5984b2-dd2a-5d11-a451-95c469c8f8a3",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Ability(
            title="Victory Star",
            game_text="Once during your turn, after you flip any coins for an attack, you may ignore all results of those coin flips and begin flipping those coins again. You can't use more than 1 Victory Star Ability each turn.",
            passive=VictoryStarPassive(),
        ),
        Attack(
            title="V-Flame",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
