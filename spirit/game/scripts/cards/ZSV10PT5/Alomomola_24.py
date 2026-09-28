from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _small_basic(card) -> bool:
    if not is_basic_pokemon(card):
        return False
    printed = card.attribute_originals.get(AttrID.HP.value, card.get_attribute(AttrID.HP, 0))
    return 0 < int(printed or 0) <= 70


def _gentle_fin_condition(board, player_id, pokemon) -> bool:
    if pokemon is not board.active_pokemon(player_id):
        return False
    bench = board.find_player_area(player_id, "bench")
    if not bench or len(bench.children) >= effective_bench_capacity(board, player_id):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_small_basic(c) for c in discard.children)


async def gentle_fin(ctx):
    """A Basic Pokemon with 70 HP or less from the discard pile onto the Bench."""
    pool = [c for c in ctx.discard_pile() if _small_basic(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Choose a Basic Pokémon with 70 HP or less")
    if picks:
        await ctx.bench_pokemon(picks[0])

card = PokemonCardDef(
    guid="8ef76fa1-dd45-565a-b5fb-32e227ce6fa1",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Ability(
            title="Gentle Fin",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may put a Basic Pok\u00e9mon with 70 HP or less from your discard pile onto your Bench.",
            activation=Activations.ONCE_PER_TURN,
            condition=_gentle_fin_condition,
            effect=gentle_fin,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
