from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.session.effects import is_basic_energy, is_pokemon_of_type


def _basic_of(type_value):
    return lambda c: is_basic_energy(c) and energy_provides_type(c, type_value)


def _p_or_m(pokemon) -> bool:
    return (is_pokemon_of_type(pokemon, PokemonTypes.PSYCHIC)
            or is_pokemon_of_type(pokemon, PokemonTypes.METAL))


def _x_boot_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and any(
        _p_or_m(p) for p in board.pokemon_in_play(player_id))


async def x_boot(ctx):
    """Up to 1 Basic [P] and up to 1 Basic [M] Energy from the deck onto your
    [P] / [M] Pokemon in any way you like, then shuffle."""
    picks = []
    for type_value, label in ((PokemonTypes.PSYCHIC.value, "[P]"), (PokemonTypes.METAL.value, "[M]")):
        picks += await ctx.search_deck(_basic_of(type_value), count=1, minimum=0,
                                       prompt=f"Choose a Basic {label} Energy card (optional).")
    targets = [p for p in ctx.my_pokemon_in_play() if _p_or_m(p)]
    if picks and targets:
        await distribute_energy(ctx, picks, targets)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="98b44f4b-30fb-5b6a-92c6-cf6dfc215701",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetagrossex.Name",
    display_name="Steven's Metagross ex",
    searchable_by=["Steven's Metagross ex", "Stage 2", "ex", "StevensMetagrossex"],
    subtypes=["Stage 2", "ex"],
    collector_number=145,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="X-Boot",
            game_text="Once during your turn, you may search your deck for a Basic [P] Energy card, a Basic [M] Energy card, or 1 of each and attach them to your [P] Pok\u00e9mon and [M] Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_x_boot_condition,
            effect=x_boot,
        ),
        Attack(
            title="Metal Stomp",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
        ),
    ],
)
