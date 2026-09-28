from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand


def _is_cynthias(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Cynthia's ")


def _cynthias_pokemon(card) -> bool:
    return is_pokemon_card(card) and _is_cynthias(card)


def _deck_not_empty(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)

card = PokemonCardDef(
    guid="6f3f95cb-e26f-59af-85dc-04cbbc4b69fa",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    display_name="Cynthia's Gabite",
    searchable_by=["Cynthia's Gabite", "Stage 1", "CynthiasGabite"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Champion's Call",
            game_text="Once during your turn, you may search your deck for a Cynthia's Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=search_to_hand(_cynthias_pokemon, count=1, reveal=True, prompt="Choose a Cynthia's Pokémon."),
        ),
        Attack(
            title="Dragonslice",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
    ],
)
