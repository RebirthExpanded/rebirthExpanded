"""Accelgor (BW - Dark Explorers 11/108 -- JP BW4 007/069, the art here).

Stage 1 Grass Pokemon (evolves from Shelmet). HP 90, weakness Fire x2,
retreat 1.

  Slam         [CC]  20
  Hit and Run  [GC]  50  Your opponent's Active Pokemon is now Poisoned
                         and Paralyzed. Shuffle this Pokemon and all cards
                         attached to it into your deck.

The conditions land before the attacker leaves (Aqua Return's shuffle);
the executor promotes a new Active afterwards.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import full_stack


async def hit_and_run(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)


card = PokemonCardDef(
    guid="f1d637c4-f909-5fbe-a5f5-d7ed7d4e8cb2",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title="Slam",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Hit and Run",
            game_text="Your opponent's Active Pokémon is now Poisoned and Paralyzed. Shuffle this Pokémon and all cards attached to it into your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=hit_and_run,
        ),
    ],
)
