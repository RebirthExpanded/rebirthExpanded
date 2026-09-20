"""Bursting Balloon (XY - BREAKpoint 97/122 -- JP XY9 073/080, the art here).

Pokemon Tool.

  "If the Pokemon this card is attached to is your Active Pokemon and is
   damaged by an opponent's attack (even if it is Knocked Out), put 6
   damage counters on the Attacking Pokemon."
  "Discard this card at the end of your opponent's turn."

Rocky Helmet with a bigger sting and a fuse: the counters are a Tool
trigger (no Ability, so an Ability lock does not reach it; Tool Jammer
does), and the discard is the Tool's own printed text, swept by the
end-of-opponent's-turn pass (discard_at_opponents_turn_end).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers

COUNTERS = 6


async def bursting_balloon(ctx):
    holder = ctx.source
    if not is_in_active_spot(holder):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == holder.owning_player_id:
        return
    await ctx.deal_damage(COUNTERS * 10, target=attacker,
                          apply_modifiers=False, as_counters=True)


card = PokemonToolCardDef(
    guid="bbfc834b-292d-5b04-a27a-1674959c3fe6",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurstingBalloon.Name",
    display_name="Bursting Balloon",
    searchable_by=["Bursting Balloon", "Item", "Pokémon Tool", "BurstingBalloon"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=97,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    discard_at_opponents_turn_end=True,
    granted_abilities=[
        Ability(
            title="Bursting Balloon",
            game_text="If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if it is Knocked Out), put 6 damage counters on the Attacking Pokémon. Discard this card at the end of your opponent's turn.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=bursting_balloon,
        ),
    ],
)
