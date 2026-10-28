"""Tinkaton (SVP 20 -- JP SV1a 043; English PAF/167, PAL/105, SVP/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_special_energy


def _gather_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(hand and hand.children and deck and deck.children)


async def gather_materials(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card from your hand")
    if paid:
        await ctx.draw_cards(3)


def _special(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="d6a384a2-9ac3-5671-aa6b-ce824e919811",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Ability(
            title="Gather Materials",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_gather_condition,
            effect=gather_materials,
        ),
        Attack(
            title="Special Hammer",
            game_text="If this Pokémon has any Special Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_special, 90),
        ),
    ],
)
