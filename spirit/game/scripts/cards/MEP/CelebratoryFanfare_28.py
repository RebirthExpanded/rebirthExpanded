"""Celebratory Fanfare (ME - Mega Promo MEP 028 -- JP MEGA Promo 033/147).

Stadium.

  "Once during each player's turn, that player may heal 10 damage from each
   of their Pokemon. If a player healed any damage in this way, their turn
   ends."

Tropical Beach's shape: offered only while something can be healed, and
the turn ends only when damage actually came off.
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.session.passives import effective_max_hp


def _anything_damaged(board, player_id, pokemon=None) -> bool:
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in board.pokemon_in_play(player_id))


async def celebratory_fanfare(ctx):
    healed = 0
    for pokemon in list(ctx.my_pokemon_in_play()):
        healed += await ctx.heal(10, pokemon) or 0
    if healed:
        ctx.ends_turn = True


card = StadiumCardDef(
    guid="dd121f94-a348-53af-a022-578adee0c891",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CelebratoryFanfare.Name",
    display_name="Celebratory Fanfare",
    searchable_by=["Celebratory Fanfare", "Stadium", "CelebratoryFanfare"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    ability=Ability(
        title="Celebratory Fanfare",
        game_text="Once during each player's turn, that player may heal 10 damage from each of their Pokémon. If a player healed any damage in this way, their turn ends.",
        activation=Activations.ONCE_PER_TURN,
        condition=_anything_damaged,
        effect=celebratory_fanfare,
    ),
)
