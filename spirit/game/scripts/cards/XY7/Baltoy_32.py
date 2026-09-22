"""Baltoy (XY - Ancient Origins 32/98 -- JP XY7 032/081, the art here).

Basic Fighting Pokemon. HP 60, weakness Grass x2, retreat 1.

  Ancient Trait  Θ Stop  Prevent all effects of your opponent's Pokemon's
                         Abilities done to this Pokemon.
  Future Sight   [C]     Look at the top 3 cards of either player's deck
                         and put them back in any order.

Θ Stop is an Ancient Trait, not an Ability, so an Ability lock leaves it
working (Malamar's shape).
"""

from spirit.game.attributes import (AbilityTypes, PokemonStage, PokemonTypes,
                                    Rarities)
from spirit.game.card_effects.passives_common import ability_effect_shield_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

LOOK = 3


async def future_sight(ctx):
    which = await ctx.choose(
        "Whose deck?", ["Your deck", "Your opponent's deck"],
        descriptions=["Look at the top 3 cards of your deck.",
                      "Look at the top 3 cards of your opponent's deck."])
    pid = ctx.player_id if which == 0 else ctx.opponent_id
    await ctx.reorder_deck_top(LOOK, player_id=pid,
                               prompt="Put the cards back in any order")


card = PokemonCardDef(
    guid="8cc55457-c640-5b27-9252-738facbf85f6",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=343,
    abilities=[
        Ability(
            title="θ Stop",
            game_text="Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
            ability_type=AbilityTypes.ANCIENT_TRAIT,
            passive=ability_effect_shield_passive(),
        ),
        Attack(
            title="Future Sight",
            game_text="Look at the top 3 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=future_sight,
        ),
    ],
)
