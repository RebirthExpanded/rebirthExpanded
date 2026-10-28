"""Slowpoke (SV2 85 -- JP SV2P 029; English PAL/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def tail_fishing(ctx):
    results = await ctx.flip_coins(1, "Tail-Fishing")
    if results and results[0]:
        picks = await ctx.search_deck(count=1, minimum=0, prompt="Choose a card to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
        await ctx.shuffle_deck()
    elif ctx.hand():
        await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card from your hand")


card = PokemonCardDef(
    guid="f4aa9a6f-2518-5c48-bfef-4888ed8f6e56",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=79,
    abilities=[
        Attack(
            title="Tail-Fishing",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck. If tails, discard a card from your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=tail_fishing,
        ),
        Attack(
            title="Zen Headbutt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)
