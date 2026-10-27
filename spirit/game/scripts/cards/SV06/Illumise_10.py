"""Illumise (SV06 10 -- JP SV6 005; English TWM/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import second_players_first_turn
from spirit.game.session.effects import full_stack


async def slowing_perfume(ctx):
    bench = [p for p in ctx.opponent_bench() if not ctx.effects_blocked(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon to shuffle into their deck")
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)


card = PokemonCardDef(
    guid="3fdf900a-b9de-52dc-8c3d-1e12d4970c57",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Attack(
            title="Slowing Perfume",
            game_text="You can use this attack only if you go second, and only during your first turn. Shuffle 1 of your opponent's Benched Pokémon and all attached cards into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=slowing_perfume,
            condition=second_players_first_turn,
        ),
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
