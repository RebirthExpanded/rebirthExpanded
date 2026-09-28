from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import subtypes_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import count_bench, damage_per


def _deck_not_empty(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


def _is_stage2(pokemon) -> bool:
    return "Stage 2" in subtypes_for(pokemon.archetype_id)

card = PokemonCardDef(
    guid="cd3514ec-b2ce-50e2-97a0-3f37253ea8f9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswineex.Name",
    display_name="Mamoswine ex",
    searchable_by=["Mamoswine ex", "Stage 2", "ex", "Mamoswineex"],
    subtypes=["Stage 2", "ex"],
    collector_number=79,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Mammoth Hauler",
            game_text="Once during your turn, you may search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=search_to_hand(is_pokemon_card, count=1, reveal=True, prompt="Choose a Pokémon to put into your hand."),
        ),
        Attack(
            title="Rumbling March",
            game_text="This attack does 40 more damage for each Stage 2 Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=180,
            damage_operator="+",
            effect=damage_per(count_bench("mine", _is_stage2), 40, base=180),
        ),
    ],
)
