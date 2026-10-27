"""Ho-Oh (ME4 10 -- JP M4 010; English CRI/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def flames_of_revival(ctx):
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    pool = [c for c in ctx.recoverable_discard() if is_basic_pokemon(c)]
    if space <= 0 or not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, space, len(pool)), minimum=0,
                                   prompt="Choose up to 3 Basic Pokémon to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="269cf519-3e77-5cf0-a019-fee6243fb089",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Attack(
            title="Flames of Revival",
            game_text="Put up to 3 Basic Pokémon from your discard pile onto your Bench.",
            cost={PokemonTypes.FIRE: 1},
            effect=flames_of_revival,
        ),
        Attack(
            title="Bright Wing",
            game_text="Discard a Fire Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 3},
            damage=130,
            effect=ac.self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)
