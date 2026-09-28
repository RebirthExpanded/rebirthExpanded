from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.support_common import search_to_hand


def _ethans_adventure(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Ethan's Adventure"


def _deck_not_empty(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)

card = PokemonCardDef(
    guid="389d5fb7-a9ff-5b86-8b65-957456f5b1bf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansQuilava.Name",
    display_name="Ethan's Quilava",
    searchable_by=["Ethan's Quilava", "Stage 1", "EthansQuilava"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansCyndaquil.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Bonded by the Journey",
            game_text="Once during your turn, you may search your deck for an Ethan's Adventure card, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=search_to_hand(_ethans_adventure, count=1, reveal=True, prompt="Choose an Ethan's Adventure card."),
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
    ],
)
