"""Delibird (MEE 10 -- JP MEE 010; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

import random
from spirit.game.session.effects import is_energy_card


def _active_with_deck(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return board.active_pokemon(player_id) is pokemon and bool(deck and deck.children)


async def energy_present(ctx):
    top = ctx.deck_top(6)
    if not top:
        return
    pool = [c for c in top if is_energy_card(c)]
    picks = await ctx.choose_cards(pool, 1, minimum=0, display_cards=top, prompt="Choose an Energy card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    rest = [c for c in top if c not in picks]
    random.shuffle(rest)
    for card in rest:
        await ctx.put_on_bottom_of_deck(card)


card = PokemonCardDef(
    guid="4274d291-ac5c-52c7-939d-6731279e7955",
    key="MEE",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MEE",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=225,
    abilities=[
        Ability(
            title="Energy Present",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Look at the top 6 cards of your deck, reveal an Energy card you find there, and put it into your hand. Shuffle the other cards and put them on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_active_with_deck,
            effect=energy_present,
        ),
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
