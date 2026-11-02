"""Pretend Galactic Boss Pikachu (SMPJ 194 -- JP SMP 194; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _destroy_the_world(ctx):
    """Flip 3 coins. Discard that many cards from the top of the opponent's deck."""
    results = await ctx.flip_coins(3, ctx.ability.title if ctx.ability else "")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="c6c280d1-b52a-54ca-abe3-384e7439944a",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendGalacticBossPikachu.Name",
    display_name="Pretend Galactic Boss Pikachu",
    searchable_by=["Pretend Galactic Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=194,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Destroy the World?",
            game_text="Flip 3 coins. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_destroy_the_world,
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
