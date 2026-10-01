"""Tremendous Bomb (ME - Abyss Eye 82 -- JP M5 073).

Pokemon Tool.

  "If the Pokemon this card is attached to isn't a Mega Evolution Pokemon
   ex, is in the Active Spot, and takes 240 or more damage from an attack
   from your opponent's Mega Evolution Pokemon ex (even if this Pokemon is
   Knocked Out), place 12 damage counters on the Attacking Pokemon. If you
   placed any damage counters in this way, discard this card."

Punk Helmet's granted ON_DAMAGED_BY_ATTACK hook, reading the damage dealt.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers, def_for, subtypes_for
from spirit.game.session.effects import full_stack, is_pokemon_tool
from spirit.game.card_effects.passives_common import hit_in_active_by_opponent


def _mega(pokemon) -> bool:
    return "SV_Mega" in subtypes_for(pokemon.archetype_id)


async def _tremendous_bomb_trigger(ctx):
    pokemon = ctx.source
    if _mega(pokemon) or not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id or not _mega(attacker):
        return
    if (getattr(ctx, "damage_amount", 0) or 0) < 240:
        return
    placed = await ctx.deal_damage(120, target=attacker, apply_modifiers=False, as_counters=True)
    if placed:
        bombs = [c for c in full_stack(pokemon) if c is not pokemon and is_pokemon_tool(c)
                 and getattr(def_for(c.archetype_id), "display_name", None) == "Tremendous Bomb"]
        if bombs:
            await ctx.discard_cards(bombs[:1])


card = PokemonToolCardDef(
    guid="1fc92cd3-91f5-53d9-b3c9-fe4cb5465426",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TremendousBomb.Name",
    display_name="Tremendous Bomb",
    searchable_by=["Tremendous Bomb", "Pokémon Tool", "Tool", "TremendousBomb"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=82,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Tremendous Bomb",
            game_text="If the Pokémon this card is attached to isn't a Mega Evolution Pokémon ex, is in the Active Spot, and takes 240 or more damage from an attack from your opponent's Mega Evolution Pokémon ex (even if this Pokémon is Knocked Out), place 12 damage counters on the Attacking Pokémon. If you placed any damage counters in this way, discard this card.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: (hit_in_active_by_opponent(c) and not _mega(c.source) and _mega(c.damaged_by) and (getattr(c, 'damage_amount', 0) or 0) >= 240),
            effect=_tremendous_bomb_trigger,
        ),
    ],
)
