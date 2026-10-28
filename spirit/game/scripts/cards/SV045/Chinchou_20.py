"""Chinchou (SV045 20 -- JP SV3a 012; English PAF/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def shine_on(ctx):
    top = list(ctx.deck_top(1))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Put that card on the bottom of your deck?"):
        await ctx.put_on_bottom_of_deck(top[0])


card = PokemonCardDef(
    guid="6fb579fc-74be-5cf7-b8b3-bbf1a3d2ba79",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=170,
    abilities=[
        Attack(
            title="Shine On",
            game_text="Look at the top card of your deck. You may put that card on the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shine_on,
        ),
        Attack(
            title="Tiny Charge",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
