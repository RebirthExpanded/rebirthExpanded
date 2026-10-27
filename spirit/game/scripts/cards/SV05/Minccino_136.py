"""Minccino (SV05 136 -- JP SV5K 059; English TEF/136, TEF/182). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_tool


async def cleaning_up(ctx):
    pool = [c for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
            for c in p.children if is_pokemon_tool(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Discard up to 2 Pokémon Tools")
        if picks:
            await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="b5e97f25-8164-583a-875b-b575fb89b55e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Cleaning Up",
            game_text="Discard up to 2 Pokémon Tools from your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=cleaning_up,
        ),
    ],
)
