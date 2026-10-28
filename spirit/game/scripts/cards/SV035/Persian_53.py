"""Persian (SV035 53 -- JP SV2a 053; English MEW/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for


def _charisma(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Giovanni's Charisma"


def _has_deck(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = PokemonCardDef(
    guid="7f488f1d-645f-5cfc-8843-bdfb4c5cc9e6",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Rocket Call",
            game_text="Once during your turn, you may search your deck for a Giovanni's Charisma card, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_deck,
            effect=su.search_to_hand(_charisma, count=1, reveal=True, prompt="Choose a Giovanni's Charisma card."),
        ),
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
