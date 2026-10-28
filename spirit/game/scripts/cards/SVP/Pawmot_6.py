"""Pawmot (SVP 6 -- JP SV1V 036; English PAF/144, SVI/209, SVI/76, SVP/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


def _has_deck(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = PokemonCardDef(
    guid="801b5ab8-4427-517b-98a5-ad64c0c9b495",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Ability(
            title="Electrogenesis",
            game_text="Once during your turn, you may search your deck for a Basic Lightning Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_deck,
            effect=su.search_attach_energy(_basic_lightning, count=1, to_self=True, prompt="Choose a Basic Lightning Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Electro Paws",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
