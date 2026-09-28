from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def pow_pow_punching(ctx):
    """10 + 30 for each heads before the first tails."""
    heads = await ctx.flip_until_tails(ctx.ability.title)
    await ctx.deal_damage(10 + 30 * heads)

card = PokemonCardDef(
    guid="c14d9899-53ab-59df-b8d6-e2c0fecdae21",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Basic", "Tyrogue"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Attack(
            title="Pow-Pow Punching",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=pow_pow_punching,
        ),
    ],
)
