"""Adversity Policy (ME - Chaos Rising 74 -- JP MEGA Promo 049).

Pokemon Tool.

  "If the Pokemon this card is attached to has Weakness to your opponent's
   Active Pokemon's type, is in the Active Spot, and is damaged by an
   attack from your opponent's Pokemon (even if this Pokemon is Knocked
   Out), draw 3 cards."

Punk Helmet's granted ON_DAMAGED_BY_ATTACK hook; the Weakness test reads
the attacker's live types (Double Type, Chromashift).
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.session.effects import live_pokemon_types
from spirit.game.card_effects.passives_common import hit_in_active_by_opponent


async def _adversity_policy_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    weak = pokemon.get_attribute(AttrID.WEAKNESS_TYPES)
    weak = weak if isinstance(weak, (list, tuple)) else [weak]
    if not any(t in live_pokemon_types(attacker) for t in weak if t is not None):
        return
    await ctx.draw_cards(3, player_id=pokemon.owning_player_id)


def _adversity_applies(ctx) -> bool:
    if not hit_in_active_by_opponent(ctx):
        return False
    weak = ctx.source.get_attribute(AttrID.WEAKNESS_TYPES)
    weak = weak if isinstance(weak, (list, tuple)) else [weak]
    return any(t in live_pokemon_types(ctx.damaged_by) for t in weak if t is not None)


card = PokemonToolCardDef(
    guid="cb5fdb98-3564-5c31-a2b6-9412649a5514",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdversityPolicy.Name",
    display_name="Adversity Policy",
    searchable_by=["Adversity Policy", "Pokémon Tool", "Tool", "AdversityPolicy"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=74,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Adversity Policy",
            game_text="If the Pokémon this card is attached to has Weakness to your opponent's Active Pokémon's type, is in the Active Spot, and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), draw 3 cards.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: _adversity_applies(c),
            effect=_adversity_policy_trigger,
        ),
    ],
)
