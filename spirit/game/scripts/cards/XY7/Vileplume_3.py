"""Vileplume (XY - Ancient Origins 3/98).

Stage 2 Grass Pokemon. HP 130, weakness Fire x2, no resistance, retreat 3.

  Ability  Irritating Pollen  Each player can't play any Item cards from
                              his or her hand.

  Solar Beam [GGC] 70

The lock is symmetrical -- "each player", its own controller included --
and it asks only that this Pokemon be in play, Active or Benched, so the
passive tests nothing about position.

What counts as an Item is era-dependent, which is why this goes through
data_utils.counts_as_item rather than a bare TRAINER_TYPE check: Tools
printed through Sword & Shield are Item cards (Float Stone's type line
says so) and Scarlet & Violet's are not. So Float Stone is locked here and
Hero's Cape is not.

This is an ABILITY lock. The engine keeps it apart from the attack-imposed
kind by construction: this one is a passive, recomputed from the board
every time trainer_play_blocked is asked, and switches off with the
Ability itself (Garbotoxin, Silent Lab, Path to the Peak). Quaking
Punch-style locks are turn-state instead, TurnState.lock_plays entries with
an expiry, which a Trainer that cancels attack effects can clear without
touching this one.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, counts_as_item
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class IrritatingPollenPassive(Passive):
    """No Item cards from either player's hand while this Pokemon is in play."""

    def blocks_trainer_play(self, card, player_id, carrier):
        return counts_as_item(card.archetype_id)


card = PokemonCardDef(
    guid="02abd07b-0cab-570b-a5ac-5156d3d3919b",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Irritating Pollen",
            game_text="Each player can't play any Item cards from his or her hand.",
            passive=IrritatingPollenPassive(),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
