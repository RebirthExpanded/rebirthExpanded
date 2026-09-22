"""Steelix (SM - Cosmic Eclipse 139/236 -- JP SM11b 034/049, the art here).

Stage 1 Metal Pokemon (evolves from Onix). HP 170, weakness Fire x2,
resistance Grass -20, retreat 4.

  Land Crusher  [MC]   50x   Discard as many Pokemon that have a Retreat
                             Cost of 4 as you like from your hand. This
                             attack does 50 damage for each card you
                             discarded in this way.
  Iron Tail     [MCC]  100x  Flip a coin until you get tails. This attack
                             does 100 damage for each heads.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_card

PER_CARD = 50
PER_HEADS = 100
RETREAT_COST = 4


def _retreat_four_pokemon(card) -> bool:
    return is_pokemon_card(card) \
        and int(card.get_attribute(AttrID.RETREAT_COST) or 0) == RETREAT_COST


async def land_crusher(ctx):
    pool = [c for c in ctx.hand() if _retreat_four_pokemon(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Discard as many Pokémon with a Retreat Cost of 4 as you like.")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.deal_damage(PER_CARD * len(picks))


async def iron_tail(ctx):
    heads = await ctx.flip_until_tails("Iron Tail")
    if heads:
        await ctx.deal_damage(PER_HEADS * heads)


card = PokemonCardDef(
    guid="d946a8a8-2c0f-5d8e-a2eb-574fff6652e9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Land Crusher",
            game_text="Discard as many Pokémon that have a Retreat Cost of 4 as you like from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=land_crusher,
        ),
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 100 damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=iron_tail,
        ),
    ],
)
