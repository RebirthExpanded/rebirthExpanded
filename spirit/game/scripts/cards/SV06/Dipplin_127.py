from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def syrup_catcher(ctx):
    """Gust 1 of the opponent's Benched Pokemon, then 70 to the new Active."""
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your opponent's new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    active = ctx.opponent_active()
    if active is not None:
        await ctx.deal_damage(70, target=active)

card = PokemonCardDef(
    guid="6eaeb6d6-4e5c-57cf-ba8e-2c1cb17cd078",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    display_name="Dipplin",
    searchable_by=["Dipplin", "Stage 1", "Dipplin"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Syrup Catcher",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot. This attack does 70 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=0,
            effect=syrup_catcher,
        ),
    ],
)
