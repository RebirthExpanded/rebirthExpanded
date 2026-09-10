"""Hisuian Heavy Ball (SWSH - Astral Radiance 146/189)."""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hisuian_heavy_ball


def has_face_down_prize(board, player_id, pokemon=None) -> bool:
    """Every clause of this card names FACE-DOWN Prize cards, so with none
    left face down it has nothing to look at. Town Map turns them all face
    up; cards that flip only some leave the rest playable, which is why this
    counts rather than asking whether Town Map was played."""
    area = board.find_player_area(player_id, "prizePile")
    return any(not c.face_up for c in (area.children if area else []))

card = ItemCardDef(
    guid="a30572d8-2b7c-56b0-961c-9cce0b4223fb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HisuianHeavyBall.Name",
    display_name="Hisuian Heavy Ball",
    searchable_by=["Hisuian Heavy Ball", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=hisuian_heavy_ball,
    condition=has_face_down_prize,
)
