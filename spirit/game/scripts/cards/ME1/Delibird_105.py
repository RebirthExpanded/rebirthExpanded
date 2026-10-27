"""Delibird (ME1 105 -- JP M1S 052; English MEG/105, MEG/152). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def quick_gift(ctx):
    picks = await ctx.search_deck(count=1, minimum=0, prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="bdec9936-7989-5c72-acf0-68648e8e0c1e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=225,
    abilities=[
        Attack(
            title="Quick Gift",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=quick_gift,
            usable_first_turn=True,
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
