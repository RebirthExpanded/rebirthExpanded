from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def spiky_knuckle(ctx):
    """200. Put 2 Darkness Energy attached to this Pokemon into your hand."""
    await ctx.deal_damage()
    picks = await ctx.select_energy_units(
        ctx.source, 2, partial=True,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.DARKNESS),
        prompt="Choose 2 Darkness Energy to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="f880c265-6c9a-52ea-8769-b64edcddd9e9",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    display_name="Grimmsnarl V",
    searchable_by=["Grimmsnarl V", "Basic", "V", "GrimmsnarlV"],
    subtypes=["Basic", "V"],
    collector_number=114,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=861,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Spiky Knuckle",
            game_text="Put 2 Darkness Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=spiky_knuckle,
        ),
    ],
)