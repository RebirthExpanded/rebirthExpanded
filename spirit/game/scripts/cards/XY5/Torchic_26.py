"""Torchic (XY - Primal Clash 26/160 -- JP XY5-Bt 018/070).

Basic Fire Pokemon. HP 50, weakness Water x2, retreat 1.

  Ancient Trait  Omega Barrage  This Pokemon may attack twice a turn.
  Flare Bonus  [R]     Discard a [R] Energy card from your hand. If you do,
                       draw 2 cards.
  Claw         [R] 20  Flip a coin. If tails, this attack does nothing.
"""

from spirit.game.attributes import (AbilityTypes, PokemonStage, PokemonTypes,
                                    Rarities)
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.pokemon import AttackTwicePassive
from spirit.game.card_effects.trainers import is_fire_energy_card
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


async def flare_bonus(ctx):
    paid = await ctx.discard_from_hand(1, predicate=is_fire_energy_card,
                                       prompt="Discard a Fire Energy card")
    if paid:
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="f787e5a8-86c6-54dc-8b6b-70453460a512",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Ability(title="Ω Barrage",
                game_text="This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)",
                ability_type=AbilityTypes.ANCIENT_TRAIT, passive=AttackTwicePassive()),
        Attack(title="Flare Bonus",
               game_text="Discard a [R] Energy card from your hand. If you do, draw 2 cards.",
               cost={PokemonTypes.FIRE: 1}, damage=0, effect=flare_bonus),
        Attack(title="Claw", game_text="Flip a coin. If tails, this attack does nothing.",
               cost={PokemonTypes.FIRE: 1}, damage=20, effect=flip_or_nothing()),
    ],
)
