"""Pikachu V-UNION -- the combined Pokemon (SWSH Promos 139-142 -- JP S8a
025-028, the art here is the four pieces together).

Lightning Pokemon V-UNION. HP 300, weakness Fighting x2, no resistance,
retreat 2. When Knocked Out, the opponent takes 3 Prize cards.

  Union Gain             [C]     Attach up to 2 [L] Energy cards from your
                                 discard pile to this Pokemon.
  Shocking Shock         [LC]    120  Flip a coin. If heads, your opponent's
                                 Active Pokemon is now Paralyzed.
  Disconnect             [LLC]   150  During your opponent's next turn, they
                                 can't play any Item cards from their hand.
  Electro Ball Together  [LLC]   250

This definition is runtime-only: it never sits in a deck or a collection.
The four physical pieces (PikachuVUNION_139..142) name it, and the
assembly rule on each piece -- "Once per game, during your turn, you may
put 4 different Pikachu V-UNION cards from your discard pile onto your
Bench" -- builds this Pokemon from them (see session/legends.py,
assemble_vunion). It cannot evolve, and when it leaves play its four
pieces go where the card would have.

The "put onto your Bench" is a rule printed on the cards, not an
Ability, so Garbotoxin, Path to the Peak and their kind do not stop it;
its Union Gain and the rest are ordinary attacks of the combined
Pokemon. The card number 143 is this pool's own for the combined face
(the real cards are 139-142); the piece scripts carry the promo numbers.
"""

from spirit.game.attributes import PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import union_gain_attack
from spirit.game.data_utils import Attack, VUnionPokemonDef
from spirit.game.session.effects import is_item_card

NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVUNION.Name"


async def disconnect(ctx):
    """150, and no Items from their hand next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


UNION_GAIN = union_gain_attack(PokemonTypes.LIGHTNING)
SHOCKING_SHOCK = Attack(
    title="Shocking Shock",
    game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
    cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
    damage=120,
    effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
)
DISCONNECT = Attack(
    title="Disconnect",
    game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
    cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
    damage=150,
    effect=disconnect,
)
ELECTRO_BALL_TOGETHER = Attack(
    title="Electro Ball Together",
    game_text="",
    cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
    damage=250,
)


card = VUnionPokemonDef(
    guid="a2a85e85-0b1f-5e73-b7fd-3c62c4208842",
    key="Promo_SWSH",
    name=NAME,
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    subtypes=["V-UNION"],
    collector_number=143,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[UNION_GAIN, SHOCKING_SHOCK, DISCONNECT, ELECTRO_BALL_TOGETHER],
)
