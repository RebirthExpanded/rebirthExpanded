from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on


async def greedy_fang(ctx):
    """70. Draw 2 cards."""
    await ctx.deal_damage()
    await ctx.draw_cards(2)

card = PokemonCardDef(
    guid="cde86047-347e-5fd6-ac01-ffa8e868a00b",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSharpedoex.Name",
    display_name="Mega Sharpedo ex",
    searchable_by=["Mega Sharpedo ex", "Stage 1", "ex", "SV_Mega", "MegaSharpedoex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=61,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Greedy Fang",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=70,
            effect=greedy_fang,
        ),
        Attack(
            title="Hungry Jaws",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            damage_operator="+",
            effect=bonus_if(lambda ctx: damage_counters_on("self")(ctx) > 0, 150),
        ),
    ],
)
