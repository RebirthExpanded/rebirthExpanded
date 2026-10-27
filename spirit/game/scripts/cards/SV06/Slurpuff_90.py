"""Slurpuff (SV06 90 -- JP SV6 052; English TWM/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def slurp_slurp(ctx):
    results = await ctx.flip_coins(2, "Slurp Slurp")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(90 * heads)
    else:
        target = ctx.opponent_active()
        if target is not None:
            await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="c5465cff-d71b-5c2c-aa80-06fd39a42212",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Attack(
            title="Slurp Slurp",
            game_text="Flip 2 coins. This attack does 90 damage for each heads. If both of them are tails,  your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=slurp_slurp,
        ),
    ],
)
