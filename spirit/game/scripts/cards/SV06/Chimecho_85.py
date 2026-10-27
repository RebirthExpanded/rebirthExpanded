"""Chimecho (SV06 85 -- JP SV6 050; English TWM/179, TWM/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def homeward_chime(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon to shuffle into your deck")
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)


card = PokemonCardDef(
    guid="ab08d256-b8e4-57bd-a61f-2e26d9b35f27",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=433,
    abilities=[
        Attack(
            title="Hyper Voice",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Homeward Chime",
            game_text="Shuffle 1 of your Benched Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=homeward_chime,
        ),
    ],
)
