"""Eelektross (SV3 69 -- JP SV3 035; English OBF/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def suction_shock(ctx):
    old = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old is None or not bench or ctx.effects_blocked(old):
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if target is None or not await ctx.switch_active(ctx.opponent_id, target):
        return
    await ctx.deal_damage(60, target=target)
    results = await ctx.flip_coins(1, "Suction Shock")
    if results and results[0] and target not in ctx.knockouts:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="1197aab4-2149-5a3d-ae48-3618f18f4a85",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=69,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Suction Shock",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. If you do, this attack does 60 damage to the new Active Pokémon, and then flip a coin. If heads, that Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=suction_shock,
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)
