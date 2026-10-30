"""Evelyn (SM - Team Up 141/181 -- JP SM8b 139/150, the art here).

Supporter.

  "You can play this card only if your opponent's Active Pokemon is a
   Stage 1 Pokemon."
  "Draw 4 cards."
"""

from spirit.game.attributes import PokemonStage, Rarities
from spirit.game.card_effects.trainers import opponent_active_is_stage
from spirit.game.data_utils import SupporterCardDef

DRAW = 4


async def evelyn(ctx):
    await ctx.draw_cards(DRAW)


card = SupporterCardDef(
    guid="2cf723f0-d7bc-5cee-81b0-216b65c1bbcd",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name",
    display_name="Evelyn",
    searchable_by=["Evelyn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    condition=opponent_active_is_stage(PokemonStage.STAGE1),
    effect=evelyn,
)
