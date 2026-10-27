"""Maushold (ME6A 100 -- JP M6a 100; English 30C/125, 30C/146). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


async def gnaw_together(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if getattr(def_for(p.archetype_id), "display_name", None) == "Maushold")
    if n <= 0:
        return
    heads = sum(1 for r in await ctx.flip_coins(n, "Gnaw Together") if r)
    if heads:
        await ctx.discard_cards(ctx.deck_top(2 * heads, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="44640eb8-4bd5-544b-9ef5-9fd856358215",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name",
    display_name="Maushold",
    searchable_by=["Maushold", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Attack(
            title="Gnaw Together",
            game_text="Flip a coin for each Maushold you have in play. For each heads, discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gnaw_together,
        ),
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
