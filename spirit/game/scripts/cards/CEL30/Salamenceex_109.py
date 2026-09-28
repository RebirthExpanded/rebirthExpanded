from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_of_type
from spirit.game.session.passives import effective_bench_capacity


async def booming_call(ctx):
    """Up to 3 [N] Basic Pokemon from your discard pile onto your Bench."""
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    pool = [c for c in ctx.discard_pile()
            if is_basic_pokemon(c) and is_pokemon_of_type(c, PokemonTypes.DRAGON)]
    if space <= 0 or not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, space, len(pool)), minimum=0,
                                   prompt="Choose up to 3 [N] Pokémon to put onto your Bench")
    for pick in picks:
        await ctx.bench_pokemon(pick)

card = PokemonCardDef(
    guid="58a2e9fe-e818-513b-9ebf-ca994e4a92e7",
    key="CEL30",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=109,
    set_code="CEL30",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Booming Call",
            game_text="Put up to 3 [N] Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=booming_call,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=240,
            effect=mill_attack(2, opponent=False),
        ),
    ],
)
