"""Antique Skull Fossil (ME - PBL 73 -- JP M5 071, the art here).

Item (fossil).

  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."

  Ability  Skull Spikes  If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.

Antique Armor Fossil's shape: FossilItemCardDef with FossilBodyPassive
(no Special Conditions, no retreat) plus the discard Ability.
ON_DAMAGED_BY_ATTACK fires before the KO'd stack moves, so a Knocked
Out holder still reads as Active.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Triggers

async def ability_effect(ctx):
    """3 damage counters on the Attacking Pokemon (Active holder only)."""
    holder = ctx.source
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == holder.owning_player_id:
        return
    if not is_in_active_spot(holder):
        return
    await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True)

card = FossilItemCardDef(
    guid="6ae751c3-3883-5828-b249-2727b9c516ad",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSkullFossil.Name",
    display_name="Antique Skull Fossil",
    searchable_by=["Antique Skull Fossil", "Item", "AntiqueSkullFossil"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Skull Spikes",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK, effect=ability_effect,
        ),
    ],
)
