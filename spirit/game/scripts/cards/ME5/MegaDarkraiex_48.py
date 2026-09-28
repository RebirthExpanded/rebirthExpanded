from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _bench_damaged(ctx) -> bool:
    return any(p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p) for p in ctx.my_bench())


async def abyss_eye(ctx):
    """Knock Out the opponent's Active if it has a Special Condition."""
    d = ctx.defender
    if d is not None and d.get_attribute(AttrID.SPECIAL_CONDITIONS) and not ctx.effects_blocked(d):
        await ctx.knock_out(d)

card = PokemonCardDef(
    guid="97036d49-156d-5b2c-90ff-d037f68bbe74",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDarkraiex.Name",
    display_name="Mega Darkrai ex",
    searchable_by=["Mega Darkrai ex", "Basic", "ex", "SV_Mega", "MegaDarkraiex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=48,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Dusk Raid",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 110 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=110,
            damage_operator="+",
            effect=bonus_if(_bench_damaged, 110),
        ),
        Attack(
            title="Abyss Eye",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, it is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=0,
            effect=abyss_eye,
        ),
    ],
)
