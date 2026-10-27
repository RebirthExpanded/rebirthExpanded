"""Shiftry (ME1 15 -- JP M1L 009; English MEG/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack


async def reversing_gust(ctx):
    results = await ctx.flip_coins(1, "Reversing Gust")
    if not (results and results[0]):
        return
    pool = [p for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to shuffle into their deck")
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)


card = PokemonCardDef(
    guid="dbd6b7e8-6e5f-5982-8c85-45a49f503b89",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Reversing Gust",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pokémon. Shuffle that Pokémon and all attached cards into their deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=reversing_gust,
        ),
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
