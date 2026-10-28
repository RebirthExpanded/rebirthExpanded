"""Tatsugiri (SV4 141 -- JP SV4M 047; English PAR/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def survival_strategy(ctx):
    picks = await ctx.search_deck(count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()
    bench = ctx.my_bench()
    if bench and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="fc6a7893-f73f-5cf3-8f0d-e27de43834d4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Survival Strategy",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=survival_strategy,
        ),
    ],
)
