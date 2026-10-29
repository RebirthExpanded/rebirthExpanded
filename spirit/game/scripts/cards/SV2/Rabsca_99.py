"""Rabsca (SV2 99 -- JP SV2P 037; English PAF/163, PAL/215, PAL/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


async def revival_blessing(ctx):
    if effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()) <= 0:
        return
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Pokémon to put onto your Bench")
        if picks:
            await ctx.bench_pokemon(picks[0])


card = PokemonCardDef(
    guid="cb50f261-a1c3-556c-9a65-2c8f84f59e9a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name",
    display_name="Rabsca",
    searchable_by=["Rabsca", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    family_id=953,
    abilities=[
        Attack(
            title="Revival Blessing",
            game_text="Put a Pokémon from your discard pile onto your Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=revival_blessing,
        ),
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
