"""Litwick (RSV10PT5 16 -- JP SV11B 015; English WHT/101, WHT/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def brighten_and_burn(ctx):
    top = list(ctx.deck_top(1))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Discard the top card of your deck?"):
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="1f104173-1650-5b14-a162-032ebb07496f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    display_name="Litwick",
    searchable_by=["Litwick", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=607,
    abilities=[
        Attack(
            title="Brighten and Burn",
            game_text="Look at the top card of your deck. You may discard that card.",
            cost={PokemonTypes.FIRE: 1},
            effect=brighten_and_burn,
        ),
    ],
)
