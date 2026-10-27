"""Reuniclus (SV05 72 -- JP SV5K 032; English TEF/171, TEF/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def summoning_gate(ctx):
    top = list(ctx.deck_top(8))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    pool = [c for c in top if is_basic_pokemon(c)]
    if pool and space > 0:
        picks = await ctx.choose_cards(pool, min(space, len(pool)), minimum=0,
                                       prompt="Choose any number of Pokémon to put onto your Bench")
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a77e8724-3856-54d3-98e3-422b3d02b000",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=72,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Summoning Gate",
            game_text="Look at the top 8 cards of your deck. You may put any number of Pokémon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=summoning_gate,
        ),
        Attack(
            title="Brain Shake",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
