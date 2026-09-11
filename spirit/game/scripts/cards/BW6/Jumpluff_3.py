"""Jumpluff (BW - Dragons Exalted 3/124 -- JP BW5 "Dragon Blade" 003/050).

Stage 2 Grass Pokemon, evolves from Skiploom. HP 90, weakness Fire x2,
resistance Water -20, retreat 0.

  Ability  Leave It to the Wind  Once during your turn (before your
                                 attack), you may return this Pokemon and
                                 all cards attached to it to your hand.
  Acrobatics  [G] 20+  Flip 2 coins. This attack does 30 more damage for
                       each heads.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.trainers import _bounce_to_hand
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


async def leave_it_to_the_wind(ctx):
    await _bounce_to_hand(ctx, [ctx.source], "Return this Pokémon to your hand",
                          attached_to_hand=True)


card = PokemonCardDef(
    guid="e0064a8e-2269-5623-bae4-5d40e9c0f15c",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[
        Ability(title="Leave It to the Wind",
                game_text="Once during your turn (before your attack), you may return this Pokémon and all cards attached to it to your hand.",
                activation=Activations.ONCE_PER_TURN, effect=leave_it_to_the_wind),
        Attack(title="Acrobatics", game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
               cost={PokemonTypes.GRASS: 1}, damage=20,
               effect=flip_damage(coins=2, bonus_per_heads=30)),
    ],
)
