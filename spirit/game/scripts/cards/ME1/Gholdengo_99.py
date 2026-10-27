"""Gholdengo (ME1 99 -- JP M1L 051; English MEG/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def all_you_can_grab(ctx):
    heads = await ctx.flip_until_tails("All-You-Can-Grab")
    if heads > 0:
        picks = await ctx.search_deck(count=heads, minimum=0,
                                      prompt=f"Choose up to {heads} cards to put into your hand.")
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="f95c24fd-a626-512a-85e7-c46cf503ae32",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name",
    display_name="Gholdengo",
    searchable_by=["Gholdengo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Attack(
            title="All-You-Can-Grab",
            game_text="Flip a coin until you get tails. Search your deck for a number of cards up to the number of heads and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=all_you_can_grab,
        ),
        Attack(
            title="Speed Attack",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
