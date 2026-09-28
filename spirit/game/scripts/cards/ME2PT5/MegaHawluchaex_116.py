from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import guts_survive_passive


async def somersault_dive(ctx):
    """120, +140 if a Stadium is in play; then discard that Stadium."""
    area = ctx.board.find_global_area("activeStadium")
    stadium_in_play = bool(area and area.children)
    await ctx.deal_damage(120 + (140 if stadium_in_play else 0))
    if stadium_in_play:
        await ctx.discard_stadium()

card = PokemonCardDef(
    guid="083b9751-5d75-58d1-99cf-80675ce18d4f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHawluchaex.Name",
    display_name="Mega Hawlucha ex",
    searchable_by=["Mega Hawlucha ex", "Basic", "ex", "SV_Mega", "MegaHawluchaex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=116,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Ability(
            title="Tenacious Body",
            game_text="If this Pok\u00e9mon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pok\u00e9mon is not Knocked Out, and its remaining HP becomes 10.",
            passive=guts_survive_passive(hp_floor=10, title="Tenacious Body", flip=True),
        ),
        Attack(
            title="Somersault Dive",
            game_text="If a Stadium is in play, this attack does 140 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=somersault_dive,
        ),
    ],
)
