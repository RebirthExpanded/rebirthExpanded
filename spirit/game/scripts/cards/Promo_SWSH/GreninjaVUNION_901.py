"""Greninja V-UNION -- the combined Pokemon (SWSH Promos 155-158 -- JP
Special Card Set 001-004/013, the art here is the four pieces together).

Water Pokemon V-UNION. HP 300, weakness Lightning x2, no resistance,
retreat 2. When Knocked Out, the opponent takes 3 Prize cards.

  Union Gain        [C]         Attach up to 2 [W] Energy cards from your
                                discard pile to this Pokemon.
  Ninja Body        (Ability)   Whenever your opponent plays an Item card
                                from their hand, prevent all effects of that
                                card done to this Pokemon.
  Aqua Edge         [W]    130
  Antidote Jutsu    (Ability)   This Pokemon can't be Poisoned.
  Twister Shuriken  [WWC]       This attack does 100 damage to each of your
                                opponent's Benched Pokemon.
  Feel the Way      (Ability)   Once during your turn, you may have your
                                opponent reveal their hand.
  Waterfall Bind    [WWC]  180  During your opponent's next turn, the
                                Defending Pokemon can't retreat.

Runtime-only: the four pieces (GreninjaVUNION_155..158) name it and the
assembly rule on each builds it from the discard pile (session/legends.py).
Its Abilities are Abilities of the combined Pokemon (locks reach them);
the assembly rule is not. Number 901 is this pool's own for the combined
face; the pieces carry the promo numbers.
"""

from spirit.game.attributes import PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, spread_damage
from spirit.game.card_effects.passives_common import (
    condition_immunity_passive, item_effect_shield_passive,
)
from spirit.game.card_effects.pokemon import union_gain_attack
from spirit.game.data_utils import Ability, Activations, Attack, VUnionPokemonDef

NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaVUNION.Name"


async def feel_the_way(ctx):
    """Your opponent reveals their hand (a view-only browser for you)."""
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)


UNION_GAIN = union_gain_attack(PokemonTypes.WATER)
NINJA_BODY = Ability(
    title="Ninja Body",
    game_text="Whenever your opponent plays an Item card from their hand, prevent all effects of that card done to this Pokémon.",
    passive=item_effect_shield_passive(),
)
AQUA_EDGE = Attack(
    title="Aqua Edge",
    game_text="",
    cost={PokemonTypes.WATER: 1},
    damage=130,
)
ANTIDOTE_JUTSU = Ability(
    title="Antidote Jutsu",
    game_text="This Pokémon can't be Poisoned.",
    passive=condition_immunity_passive(SpecialConditions.POISONED),
)
TWISTER_SHURIKEN = Attack(
    title="Twister Shuriken",
    game_text="This attack does 100 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
    effect=spread_damage(100),
)
FEEL_THE_WAY = Ability(
    title="Feel the Way",
    game_text="Once during your turn, you may have your opponent reveal their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=feel_the_way,
)
WATERFALL_BIND = Attack(
    title="Waterfall Bind",
    game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
    cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
    damage=180,
    effect=condition_attack(no_retreat=True),
)


card = VUnionPokemonDef(
    guid="fe0cc249-96ca-538d-b4e4-19ff70a4e421",
    key="Promo_SWSH",
    name=NAME,
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    subtypes=["V-UNION"],
    collector_number=901,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=300,
    elements=[PokemonTypes.WATER],
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=658,
    abilities=[UNION_GAIN, NINJA_BODY, AQUA_EDGE, ANTIDOTE_JUTSU,
               TWISTER_SHURIKEN, FEEL_THE_WAY, WATERFALL_BIND],
)
