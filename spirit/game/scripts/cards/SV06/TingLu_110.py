from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ground_crasher(ctx):
    """30; with a Stadium in play, 30 to each opposing Benched Pokemon too,
    then discard that Stadium."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() is None:
        return
    for pokemon in list(ctx.opponent_bench()):
        await ctx.deal_damage(30, target=pokemon)
    await ctx.discard_stadium()

card = PokemonCardDef(
    guid="79fa89c5-5102-5e0c-ae11-cefbc997214b",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name",
    display_name="Ting-Lu",
    searchable_by=["Ting-Lu", "Basic", "TingLu"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Attack(
            title="Ground Crasher",
            game_text="If a Stadium is in play, this attack also does 30 damage to each of your opponent's Benched Pok\u00e9mon, and discard that Stadium. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ground_crasher,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
