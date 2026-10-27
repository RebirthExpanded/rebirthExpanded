"""Scraggy (ME6A 78 -- JP M6a 078; English 30C/140, 30C/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def nitpick(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.opponent_id)
    else:
        await ctx.shuffle_deck(ctx.opponent_id)
    await ctx.draw_cards(4, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="2a85c88b-a51a-5f45-a76c-c05cfa5c923d",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Nitpick",
            game_text="Your opponent shuffles their hand into their deck and draws 4 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=nitpick,
        ),
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
