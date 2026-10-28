"""Fearow (SV035 22 -- JP SV2a 022; English MEW/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def beak_catch(ctx):
    picks = await ctx.search_deck(count=3, minimum=0, prompt="Choose up to 3 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="f1fe33d0-90cb-5bd5-b0cf-2090bc868749",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow",
    searchable_by=["Fearow", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=21,
    abilities=[
        Attack(
            title="Beak Catch",
            game_text="Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=beak_catch,
        ),
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
