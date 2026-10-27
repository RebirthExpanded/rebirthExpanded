"""Swoobat (RSV10PT5 37 -- JP SV11W 034; English WHT/120, WHT/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def happy_return(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to put into your hand")
    if target is not None:
        await ctx.put_in_hand(full_stack(target), reveal=False)


card = PokemonCardDef(
    guid="2c5cbd58-8bb1-5b4a-a04e-856e59932fa6",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Happy Return",
            game_text="Put 1 of your Benched Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=happy_return,
        ),
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
