"""Gimmighoul (ME6A 67 -- JP M6a 067; English 30C/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def strolls_so_much(ctx):
    results = await ctx.flip_coins(1, "Strolls So Much")
    if results and results[0]:
        picks = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ffa740b5-d9e2-56e8-81df-a6837b3a3adf",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=999,
    abilities=[
        Attack(
            title="Strolls So Much",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=strolls_so_much,
        ),
    ],
)
