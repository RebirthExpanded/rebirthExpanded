"""Solgaleo (ME6A 84 -- JP M6a 084; English 30C/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)



def _sunrise_ok(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    deck = board.find_player_area(player_id, "deck")
    return bench is not None and pokemon.parent is bench and bool(deck and deck.children)


card = PokemonCardDef(
    guid="d3e73c93-498b-5ed9-8891-0298e2af9345",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name",
    display_name="Solgaleo",
    searchable_by=["Solgaleo", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=84,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Sunrise",
            game_text="Once during your turn, if this Pokémon is on your Bench, you may use this Ability. Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_sunrise_ok,
            effect=su.search_attach_energy(_basic_metal, count=2, to_self=True, prompt="Choose up to 2 Basic Metal Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Sunsteel Strike",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
