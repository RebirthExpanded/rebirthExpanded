"""Claydol (SV - Obsidian Flames 095/197 -- JP SV3 050/108, the art here).

Stage 1 Fighting Pokemon (evolves from Baltoy). HP 120, weakness Grass
x2, resistance Lightning -30, retreat 1.

  Doll Blast    [FFC]  Put damage counters on your opponent's Active
                       Pokemon until its remaining HP is 10. This Pokemon
                       does 120 damage to itself.
  Psycho Trip   [FC] 30  Your opponent's Active Pokemon is now Confused.

The counters are set to leave exactly 10 HP, so a target already at or
below 10 takes none; the recoil lands whatever happened.
"""

from spirit.game.attributes import (AttrID, PokemonStage, PokemonTypes,
                                    Rarities, SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

LEAVE_HP = 10
RECOIL = 120


async def doll_blast(ctx):
    target = ctx.defender
    if target is not None:
        remaining = int(target.get_attribute(AttrID.HP) or 0)
        gap = remaining - LEAVE_HP
        if gap > 0:
            await ctx.deal_damage(gap, target=target, as_counters=True,
                                  apply_modifiers=False)
    await ctx.deal_damage(RECOIL, target=ctx.attacker, apply_modifiers=False,
                          is_attack=False)


card = PokemonCardDef(
    guid="f6fa89aa-a647-5b3c-a1af-e792c6940128",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Doll Blast",
            game_text="Put damage counters on your opponent's Active Pokémon until its remaining HP is 10. This Pokémon does 120 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=doll_blast,
        ),
        Attack(
            title="Psycho Trip",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
