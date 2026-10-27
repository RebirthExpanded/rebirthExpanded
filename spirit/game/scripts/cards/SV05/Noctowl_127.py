"""Noctowl (SV05 127 -- JP SV5K 055; English TEF/127). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def talon_hunt(ctx):
    await ctx.deal_damage()
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Search your deck for up to 2 cards?"):
        return
    picks = await ctx.search_deck(count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b45e1f7f-a714-5072-8da5-a5706d2dcbd8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="Talon Hunt",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=talon_hunt,
        ),
    ],
)
