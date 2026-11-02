"""Pretend Skull Boss Pikachu (SMPJ 197 -- JP SMP 197; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _smash_it(ctx):
    """Before doing damage, discard a Pokemon Tool from the opponent's Active."""
    defender = ctx.opponent_active()
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [t for t, p in ctx.tools_in_play() if p is defender]
        if len(tools) > 1:
            tools = await ctx.choose_cards(tools, 1, minimum=1, prompt="Choose a Pokémon Tool to discard")
        if tools:
            await ctx.discard_cards(tools[:1])
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="d14091c2-08e2-5d02-a556-8de3c96ffeb8",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendSkullBossPikachu.Name",
    display_name="Pretend Skull Boss Pikachu",
    searchable_by=["Pretend Skull Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=197,
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
            title="Smash It?",
            game_text="Before doing damage, discard a Pokémon Tool from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_smash_it,
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
