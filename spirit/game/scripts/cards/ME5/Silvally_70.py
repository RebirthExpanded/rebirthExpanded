"""Silvally (ME5 70 -- JP M5 068; English PBL/70, PBL/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_supporter_card


def _call_ok(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return not (hand.children if hand else []) and bool(deck and deck.children)


card = PokemonCardDef(
    guid="0c4e3ad8-b0a4-53ea-ab52-1263357f0cba",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silvally.Name",
    display_name="Silvally",
    searchable_by=["Silvally", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Ability(
            title="Call a Buddy",
            game_text="Once during your turn, if you have no cards in your hand, you may use this Ability. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_call_ok,
            effect=su.search_to_hand(is_supporter_card, count=1, reveal=True, prompt="Choose a Supporter card."),
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
