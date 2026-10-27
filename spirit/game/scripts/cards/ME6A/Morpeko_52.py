"""Morpeko (ME6A 52 -- JP M6a 052; English 30C/135, 30C/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def select_a_snack(ctx):
    top = ctx.deck_top(3)
    if not top:
        return
    await ctx.discard_cards(top)
    picks = await ctx.choose_cards(top, 1, minimum=1, prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="df124951-adf3-50c0-a2ee-e84625367eb0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Attack(
            title="Select a Snack",
            game_text="Discard the top 3 cards of your deck and put 1 of them into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=select_a_snack,
        ),
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)
