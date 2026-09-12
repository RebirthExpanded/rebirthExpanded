"""Team Rocket's Porygon-Z (SV - Destined Rivals 155/182 -- JP SV10 083/099, the art here).

Stage 2 Colorless Pokemon, evolves from Team Rocket's Porygon2. HP 140,
weakness Fighting x2, no resistance, retreat 1.

  Ability  Reconstitute  You must discard 2 cards from your hand in order
                         to use this Ability. Once during your turn, you
                         may draw a card.
  R Command [CC] 20x  This attack does 20 damage for each Supporter card
                      that has "Team Rocket" in its name in your discard
                      pile.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_discard, damage_per
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, def_for
from spirit.game.session.effects import is_supporter_card


def _team_rocket_supporter(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_supporter_card(card) and "Team Rocket" in name


def _reconstitute_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(hand) and len(hand.children) >= 2 and bool(deck) and bool(deck.children)


async def reconstitute(ctx):
    picks = await ctx.discard_from_hand(2, minimum=2, prompt="Discard 2 cards from your hand")
    if len(picks or []) < 2:
        return
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="be05b674-48ab-53ad-8f1f-ef3af9117ebc",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygonZ.Name",
    display_name="Team Rocket's Porygon-Z",
    searchable_by=["Team Rocket's Porygon-Z", "Stage 2", "TeamRocketsPorygonZ"],
    subtypes=["Stage 2"],
    collector_number=155,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon2.Name",
    family_id=137,
    abilities=[
        Ability(title="Reconstitute",
                game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may draw a card.",
                activation=Activations.ONCE_PER_TURN,
                condition=_reconstitute_condition, effect=reconstitute),
        Attack(title="R Command",
               game_text="This attack does 20 damage for each Supporter card that has \"Team Rocket\" in its name in your discard pile.",
               cost={PokemonTypes.COLORLESS: 2},
               damage=20, damage_operator="x",
               effect=damage_per(count_discard("mine", _team_rocket_supporter), 20)),
    ],
)
