from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def flail_around(ctx):
    """10 for each heads of 3 coins."""
    heads = sum(1 for r in await ctx.flip_coins(3, ctx.ability.title) if r)
    if heads:
        await ctx.deal_damage(10 * heads)

card = PokemonCardDef(
    guid="ebc6bf87-29c8-5e59-b331-ad0a913a54cf",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    display_name="Nymble",
    searchable_by=["Nymble", "Basic", "Nymble"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=919,
    abilities=[
        Attack(
            title="Flail Around",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=flail_around,
        ),
    ],
)
