"""Pokemon Ranger (XY - Steam Siege 113/114 -- JP XY11-Br 054/054).

Supporter.

  "Remove all effects of attacks on each player and each of their Pokemon."

What goes: everything an attack left behind -- attack locks (a Defending
Pokemon that "can't attack", and the attacker's own "can't use this attack
next turn"), retreat locks, Item/Supporter locks an ATTACK imposed on a
player, Energy-attachment restrictions, Smokescreen-style flip checks,
scheduled Knock Outs (Pale Moon-GX), damage reductions and boosts granted
by attacks, and the "for the rest of this game" pieces of a GX attack
(Altered Creation-GX's +30 and extra Prize).

What stays: Special Conditions and damage (neither is an "effect of an
attack"), and anything an Ability or Trainer put in place -- Garbotoxin's
Ability lock, an Item lock from an Ability, a Supporter's coin choice.
The engine keeps a ledger of which entries the attacks wrote
(TurnState.attack_effects) so the two are never confused.

With no effect of an attack in force on either side, Ranger would do
nothing, so it can't be played then.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


def _any_attack_effect(board, player_id, card=None) -> bool:
    turn_state = getattr(board, "turn_state", None)
    return turn_state is not None and turn_state.has_attack_effects(board)


async def pokemon_ranger(ctx):
    ctx.session.turn_state.clear_attack_effects(ctx.board)


card = SupporterCardDef(
    guid="11a874d9-231b-51d7-8a51-99f5966acb4e",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRanger.Name",
    display_name="Pokémon Ranger",
    searchable_by=["Pokémon Ranger", "Supporter", "PokemonRanger"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    condition=_any_attack_effect,
    effect=pokemon_ranger,
)
