"""Picnic Basket (SV - Scarlet & Violet 184/198 -- JP SV1V 071/078, the art here).

Item.

  "Heal 30 damage from each Pokemon (both yours and your opponent's)."

Every Pokemon in play on both sides, through ctx.heal -- so a heal lock
(Heal Block, Mimikyu SWSH3's Heal Jamming) or a Stadium shield (New Moon
side: nothing; Big Tree Hill: nobody) decides per Pokemon.
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.passives import effective_max_hp


def _condition(board, player_id, pokemon=None) -> bool:
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for pid in board.player_ids for p in board.pokemon_in_play(pid))


async def picnic_basket(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        for pokemon in list(ctx.board.pokemon_in_play(pid)):
            await ctx.heal(30, pokemon)


card = ItemCardDef(
    guid="a4f57306-cc02-5530-b425-eeb8eecfb714",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PicnicBasket.Name",
    display_name="Picnic Basket",
    searchable_by=["Picnic Basket", "Item", "PicnicBasket"],
    subtypes=["Item"],
    collector_number=184,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=picnic_basket,
)
