"""Revavroom (SVP 8 -- JP SV1S 061; English PAF/193, PAF/65, SVI/142, SVP/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


def _engine_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_energy_card(c) for c in hand.children)


async def rumbling_engine(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=is_energy_card, prompt="Discard an Energy card")
    if paid:
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="46be0f21-0548-5688-a524-113590cd8799",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name",
    display_name="Revavroom",
    searchable_by=["Revavroom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Ability(
            title="Rumbling Engine",
            game_text="You must discard an Energy card from your hand in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_engine_condition,
            effect=rumbling_engine,
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=ac.flip_bonus(90),
        ),
    ],
)
