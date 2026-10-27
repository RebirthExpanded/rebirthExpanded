"""Chandelure (SV06 38 -- JP SV6 021; English TWM/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _has_deck(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def alluring_light(ctx):
    await ctx.draw_cards(1)
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="e5a11727-464b-5e2e-9860-95efbb96a28d",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Alluring Light",
            game_text="Once during your turn, you may have each player draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_deck,
            effect=alluring_light,
        ),
        Attack(
            title="Mind Ruler",
            game_text="This attack does 30 damage for each card in your opponent's hand.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_hand("opponent"), 30),
        ),
    ],
)
