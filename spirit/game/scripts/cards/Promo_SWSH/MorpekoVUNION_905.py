"""Morpeko V-UNION -- the combined Pokemon (SWSH Promos 215-218 -- JP
VMAX Climax 056-059/184, the art here is the four pieces together).

Lightning Pokemon V-UNION. HP 310, weakness Fighting x2, no resistance,
retreat 2. When Knocked Out, the opponent takes 3 Prize cards.

  Union Gain      [C]         Attach up to 2 [L] Energy cards from your
                              discard pile to this Pokemon.
  All You Can Eat [CC]        Draw cards until you have 10 cards in your
                              hand.
  Burst Wheel     [LCC] 100x  Discard all Energy from this Pokemon. This
                              attack does 100 damage for each card you
                              discarded in this way.
  Electric Ball   [LCC] 160

Runtime-only: the four pieces (MorpekoVUNION_215..218) name it and the
assembly rule on each builds it from the discard pile (session/legends.py).
Number 905 is this pool's own for the combined face.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import union_gain_attack
from spirit.game.data_utils import Attack, VUnionPokemonDef

NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVUNION.Name"


async def all_you_can_eat(ctx):
    await ctx.draw_until(10)


async def burst_wheel(ctx):
    """Every attached Energy card goes; 100 for each card (not each unit)."""
    discarded = await ctx.discard_energy_from(ctx.attacker, 99)
    if discarded:
        await ctx.deal_damage(100 * len(discarded))


UNION_GAIN = union_gain_attack(PokemonTypes.LIGHTNING)
ALL_YOU_CAN_EAT = Attack(
    title="All You Can Eat",
    game_text="Draw cards until you have 10 cards in your hand.",
    cost={PokemonTypes.COLORLESS: 2},
    effect=all_you_can_eat,
)
BURST_WHEEL = Attack(
    title="Burst Wheel",
    game_text="Discard all Energy from this Pokémon. This attack does 100 damage for each card you discarded in this way.",
    cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
    damage=100,
    damage_operator="x",
    effect=burst_wheel,
)
ELECTRIC_BALL = Attack(
    title="Electric Ball",
    game_text="",
    cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
    damage=160,
)


card = VUnionPokemonDef(
    guid="88a75827-1c70-5950-9310-98d262ccead5",
    key="Promo_SWSH",
    name=NAME,
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    subtypes=["V-UNION"],
    collector_number=905,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[UNION_GAIN, ALL_YOU_CAN_EAT, BURST_WHEEL, ELECTRIC_BALL],
)
