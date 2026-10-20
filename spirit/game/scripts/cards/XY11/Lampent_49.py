"""Lampent (XY - Steam Siege 49/114 -- JP XY11-Bb 026/054, the art here).

Stage 1 Psychic Pokemon (evolves from Litwick). HP 80, weakness Darkness
x2, resistance Fighting -20, retreat 1.

  Mirror Mirror      [C]      Each player either draws or discards cards
                              until that player has 4 cards in his or her
                              hand. (Your opponent does this first.)
  Flickering Flames  [P][C]  20  Your opponent's Active Pokemon is now Asleep.

Each player picks their own discards.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.data_utils import Attack, PokemonCardDef


async def _to_four(ctx, player_id):
    size = len(ctx.hand(player_id))
    if size < 4:
        await ctx.draw_cards(4 - size, player_id=player_id)
    elif size > 4:
        await ctx.discard_from_hand(
            size - 4, minimum=size - 4, player_id=player_id,
            prompt="Discard cards until you have 4 cards in your hand.")


async def mirror_mirror(ctx):
    await _to_four(ctx, ctx.opponent_id)
    await _to_four(ctx, ctx.player_id)


async def flickering_flames(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="261a6a19-77ec-5e81-90be-90a07df6a14b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Mirror Mirror",
            game_text="Each player either draws or discards cards until that player has 4 cards in his or her hand. (Your opponent does this first.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mirror_mirror,
        ),
        Attack(
            title="Flickering Flames",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flickering_flames,
        ),
    ],
)
