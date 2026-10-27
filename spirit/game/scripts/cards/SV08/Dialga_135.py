"""Dialga (SV08 135 -- JP SV7a 042; English SSP/135). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def time_manipulation(ctx):
    picks = await ctx.search_deck(count=2, minimum=0, prompt="Choose 2 cards to put on top of your deck.")
    await ctx.shuffle_deck()
    for card in reversed(picks):
        await ctx.put_on_top_of_deck(card)
    if len(picks) > 1:
        await ctx.reorder_deck_top(len(picks))


card = PokemonCardDef(
    guid="8ed8dcbf-1015-5165-a189-6cdf24f924d6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=483,
    abilities=[
        Attack(
            title="Time Manipulation",
            game_text="Search your deck for 2 cards, shuffle your deck, then put those cards on top of it in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=time_manipulation,
        ),
        Attack(
            title="Buster Tail",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
