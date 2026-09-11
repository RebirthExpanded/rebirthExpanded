"""Vivillon (Perfect Order 9/... -- JP M3 009/080).

Stage 2 Grass Pokemon, evolves from Spewpa. HP 120, weakness Fire x2,
retreat 1, regulation mark J.

  Ability  Grand Wing  Once during your turn, you may use this Ability.
                       Your opponent shuffles their hand and puts it on the
                       bottom of their deck. If they put any cards on the
                       bottom of their deck in this way, they draw 4 cards.
  Blow Through  [G] 60+  If a Stadium is in play, this attack does 60 more
                         damage.

The draw is conditional on the shuffle having moved anything, so an empty
hand opposite means no cards go under the deck and none are drawn -- the
Ability is a reset, not a gift.

"If a Stadium is in play" is any Stadium, either player's, which is why the
attack reads the shared Stadium slot rather than a Stadium of your own.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


async def grand_wing(ctx):
    """Their hand goes under their deck; if any of it did, they draw 4."""
    moved = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    if not moved:
        return
    await ctx.draw_cards(4, player_id=ctx.opponent_id)


def _stadium_in_play(ctx) -> bool:
    area = ctx.board.find_global_area("activeStadium")
    return bool(area and area.children)


async def blow_through(ctx):
    """60, and 60 more with any Stadium on the table."""
    await ctx.deal_damage(120 if _stadium_in_play(ctx) else 60)


card = PokemonCardDef(
    guid="acb4ee74-01d0-5f1f-8e4a-0b91919abfe1",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Grand Wing",
            game_text="Once during your turn, you may use this Ability. Your opponent shuffles their hand and puts it on the bottom of their deck. If they put any cards on the bottom of their deck in this way, they draw 4 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=grand_wing,
        ),
        Attack(
            title="Blow Through",
            game_text="If a Stadium is in play, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=blow_through,
        ),
    ],
)
