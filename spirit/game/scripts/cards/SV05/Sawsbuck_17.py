"""Sawsbuck (SV05 17 -- JP SV5M 009; English TEF/166, TEF/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_stadium_card


def _has_deck(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = PokemonCardDef(
    guid="b4a27c35-6be2-5189-8aec-822ab19bcae3",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Ability(
            title="Changing Seasons",
            game_text="Once during your turn, you may search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_deck,
            effect=su.search_to_hand(is_stadium_card, count=1, reveal=True, prompt="Choose a Stadium card."),
        ),
        Attack(
            title="Superpowered Horns",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
