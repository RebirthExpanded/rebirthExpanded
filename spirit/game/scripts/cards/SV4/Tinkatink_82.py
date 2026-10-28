"""Tinkatink (SV4 82 -- JP SV4M 034; English PAR/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def mountain_scrounging(ctx):
    top = list(ctx.deck_top(1))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Put that card into your hand? (No: discard it and draw a card)"):
        await ctx.put_in_hand(top, reveal=False)
    else:
        await ctx.discard_cards(top)
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="90b7c173-0298-5dd3-ae0d-d60f407a2e4d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Mountain Scrounging",
            game_text="Look at the top card of your deck. You may put that card into your hand. If you don't, discard that card and draw a card.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=mountain_scrounging,
        ),
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
