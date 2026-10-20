"""Butterfree (SV - Journey Together 3/159 -- JP SV9 003/100, the art here).

Stage 2 Grass Pokemon (evolves from Metapod). HP 120, weakness Fire x2,
retreat 1.

  Scale Hurricane  [G]  60x  Flip 4 coins. This attack does 60 damage for
                             each heads. If at least 2 of them are heads,
                             your opponent's Active Pokemon is now Paralyzed.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.data_utils import Attack, PokemonCardDef


async def scale_hurricane(ctx):
    results = await ctx.flip_coins(4, "Scale Hurricane")
    heads = sum(1 for r in results if r)
    if heads > 0:
        await ctx.deal_damage(heads * 60)
    if heads >= 2:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="f4bd165d-1860-5c56-a541-c0d543b6b139",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Scale Hurricane",
            game_text="Flip 4 coins. This attack does 60 damage for each heads. If at least 2 of them are heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="x",
            effect=scale_hurricane,
        ),
    ],
)
