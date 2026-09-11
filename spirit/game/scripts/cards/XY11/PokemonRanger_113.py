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
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


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
    effect=pokemon_ranger,
)
