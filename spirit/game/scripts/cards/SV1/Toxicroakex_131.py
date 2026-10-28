"""Toxicroak ex (SV1 131 -- JP SV1S 055; English SVI/131, SVI/232). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def nasty_plot(ctx):
    picks = await ctx.search_deck(count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a3c2d5e2-f1dc-5b82-811a-164690b5fc6f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroakex.Name",
    display_name="Toxicroak ex",
    searchable_by=["Toxicroak ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=131,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=nasty_plot,
        ),
        Attack(
            title="Toxic Ripper",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 6 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ac.condition_attack(SpecialConditions.POISONED, counters=6),
        ),
    ],
)
