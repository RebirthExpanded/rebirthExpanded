"""Scrafty (SVP 188 -- JP SVP 158; English SVP/188). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def nab_n_dash(ctx):
    n = len(ctx.my_bench())
    if n:
        picks = await ctx.search_deck(count=n, minimum=0, prompt=f"Choose up to {n} cards to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d1cfcf4d-75c6-57e7-880c-37bce6bdf88f",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=188,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Nab 'n' Dash",
            game_text="Search your deck for a number of cards up to the number of your Benched Pokémon and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=nab_n_dash,
        ),
        Attack(
            title="High Jump Kick",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
