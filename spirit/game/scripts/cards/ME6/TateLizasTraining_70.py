"""Tate & Liza's Training (ME6 70 -- JP M6 070; English Japan only). Japanese art.

Draw 2 cards. Then, if a Stadium with "Legendary" in its name is in play, put this card into your hand instead of the discard pile.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for


def _legendary_stadium(board) -> bool:
    area = board.find_global_area("activeStadium")
    return any("Legendary" in (getattr(def_for(c.archetype_id), "display_name", "") or "")
               for c in (area.children if area else []))
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def tate_and_lizas_training(ctx):
    await ctx.draw_cards(2)
    source = ctx.source
    parent = getattr(source, "parent", None)
    played = (getattr(ctx, "is_trainer_effect", False) and parent is not None
              and parent.get_attribute(AttrID.NAME) == "activeTrainer")
    if played and _legendary_stadium(ctx.board):
        await ctx.put_in_hand([source], reveal=True)


card = SupporterCardDef(
    guid="6744be55-618d-5ffc-9093-92e6886a2be7",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLizasTraining.Name",
    display_name="Tate & Liza's Training",
    searchable_by=["Tate & Liza's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=70,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=tate_and_lizas_training,
)
