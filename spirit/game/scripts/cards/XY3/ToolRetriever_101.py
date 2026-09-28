"""Tool Retriever (XY - Furious Fists 101/111 -- JP XY3 083/096).

Item.

  "Put up to 2 Pokemon Tool cards attached to your Pokemon into your hand."

Not playable with no Tool on any of your Pokemon.
"""

from spirit.game.attributes import AttrID, Rarities, TrainerType
from spirit.game.data_utils import ItemCardDef


# Pokemon Tool, XY "Pokemon Tool F", and SV Technical Machines (Tools too).
_TOOL_TYPES = {TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
               TrainerType.TECHNICAL_MACHINE.value}


def _your_tools(board, player_id):
    tools = []
    for pokemon in board.pokemon_in_play(player_id):
        for child in pokemon.children:
            if child.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES:
                tools.append(child)
    return tools


def _has_tool(board, player_id, card=None) -> bool:
    return bool(_your_tools(board, player_id))


async def tool_retriever(ctx):
    tools = _your_tools(ctx.board, ctx.player_id)
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, min(2, len(tools)), minimum=1,
        prompt="Choose up to 2 Pokémon Tools to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="3b937825-f73d-5df2-b236-6a7dfd2b85b1",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolRetriever.Name",
    display_name="Tool Retriever",
    searchable_by=["Tool Retriever", "Item", "ToolRetriever"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    condition=_has_tool,
    effect=tool_retriever,
)
