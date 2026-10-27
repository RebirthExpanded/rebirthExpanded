"""Iono's Electrode (SV09 48 -- JP SV9 027; English JTG/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def thump_thump_boom(ctx):
    await ctx.deal_damage(100, target=ctx.attacker, apply_modifiers=False)
    results = await ctx.flip_coins(1, "Thump-Thump Boom")
    target = ctx.opponent_active()
    if results and results[0] and target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="a9a06191-683a-5f25-bc56-7f5de74194c8",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosElectrode.Name",
    display_name="Iono's Electrode",
    searchable_by=["Iono's Electrode", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosVoltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Thump-Thump Boom",
            game_text="This Pokémon does 100 damage to itself. Flip a coin. If heads, your opponent's Active Pokémon is Knocked Out.",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=thump_thump_boom,
        ),
        Attack(
            title="Electric Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
