from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_protection


async def slight_splash(ctx):
    """Flip; heads: no damage from or effects of attacks next turn."""
    if (await ctx.flip_coins(1, ctx.ability.title))[0]:
        await apply_protection(ctx, prevent=True, effects_too=True)

card = PokemonCardDef(
    guid="f39ef501-1538-59b5-acd1-bcbc5d7fa760",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    display_name="Nymble",
    searchable_by=["Nymble", "Basic", "Nymble"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=919,
    abilities=[
        Attack(
            title="Slight Splash",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=slight_splash,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
