"""Team Rocket's Hypnotizer (ME - Ascended Heroes 206 -- JP SV-P 267).

Pokemon Tool.

  "If the Team Rocket's Pokemon this card is attached to is in the Active
   Spot and is damaged by an attack from your opponent's Pokemon (even if
   this Team Rocket's Pokemon is Knocked Out), the Attacking Pokemon is now
   Asleep."

Punk Helmet's granted ON_DAMAGED_BY_ATTACK hook.
"""

from spirit.game.attributes import Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers, def_for
from spirit.game.card_effects.passives_common import hit_in_active_by_opponent


async def _hypnotizer_trigger(ctx):
    pokemon = ctx.source
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    if not name.startswith("Team Rocket's ") or not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.ASLEEP)


card = PokemonToolCardDef(
    guid="a9b2c920-1361-59d2-b34c-e11667e21eb5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHypnotizer.Name",
    display_name="Team Rocket's Hypnotizer",
    searchable_by=["Team Rocket's Hypnotizer", "Pokémon Tool", "Tool", "TeamRocketsHypnotizer"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=206,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Team Rocket's Hypnotizer",
            game_text="If the Team Rocket's Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Team Rocket's Pokémon is Knocked Out), the Attacking Pokémon is now Asleep.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: hit_in_active_by_opponent(c) and (getattr(def_for(c.source.archetype_id), 'display_name', '') or '').startswith("Team Rocket's "),
            effect=_hypnotizer_trigger,
        ),
    ],
)
