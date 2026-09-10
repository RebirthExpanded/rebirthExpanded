"""Weavile-GX (SM - Unified Minds 132/236).

Stage 1 Darkness Pokemon-GX. HP 200, weakness Fighting x2, resistance
Psychic -20, retreat 1.

  Ability  Shadow Connection  As often as you like during your turn
                              (before your attack), you may move a basic
                              Darkness Energy from 1 of your Pokemon to
                              another of your Pokemon.

  Claw Slash            [DDC] 130
  Nocturnal Maneuvers-GX [C]   Search your deck for any number of Basic
                              Pokemon and put them onto your Bench. Then,
                              shuffle your deck.

Shadow Connection is Mega Venusaur ex's Solar Transfer in Darkness, so it
runs the same move_energy_freely loop: one use keeps offering the next
Energy and the player declines when done, rather than closing after each
single move.

"Any number of Basic Pokemon" is the Bench's own limit, so the GX attack
asks for a full Bench's worth and search_to_bench caps it at the space
actually free -- which now reads the effective Bench, so Collapsed Stadium
narrows it.

The pool's first Unified Minds card, so SM11 joins the Expanded set list
(it was already in sets.json as UNM).
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import is_basic_pokemon


def _is_basic_darkness_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.DARKNESS.value)


def _shadow_connection_condition(board, player_id, pokemon=None):
    """Two Pokemon of yours in play and a basic Darkness Energy on one."""
    in_play = board.pokemon_in_play(player_id)
    if len(in_play) < 2:
        return False
    return any(any(_is_basic_darkness_energy(e) for e in p.children)
               for p in in_play)


async def shadow_connection(ctx):
    """Move basic Darkness Energy around your board until the player is done."""
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(
        pokemon, pokemon, predicate=_is_basic_darkness_energy,
        prompt="Choose a basic Darkness Energy to move (or Done)",
    )


card = PokemonCardDef(
    guid="52f772e3-f647-572d-8ab2-06855c104e83",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavilegx.Name",
    display_name="Weavile-GX",
    searchable_by=["Weavile-GX", "Stage 1", "GX", "Weavilegx"],
    subtypes=["Stage 1", "GX"],
    collector_number=132,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Shadow Connection",
            game_text=(
                "As often as you like during your turn (before your attack), "
                "you may move a basic Darkness Energy from 1 of your Pokémon "
                "to another of your Pokémon."
            ),
            activation=Activations.UNLIMITED,
            condition=_shadow_connection_condition,
            effect=shadow_connection,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Nocturnal Maneuvers-GX",
            game_text=(
                "Search your deck for any number of Basic Pokémon and put "
                "them onto your Bench. Then, shuffle your deck. (You can't "
                "use more than 1 GX attack in a game.)"
            ),
            cost={PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=search_to_bench(
                predicate=is_basic_pokemon, count=BENCH_CAPACITY,
                prompt="Choose Basic Pokémon to put onto your Bench.",
            ),
        ),
    ],
)
