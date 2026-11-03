"""Victini (XYPJ 248 -- JP XYP 248; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

_discard_all = ac.self_energy_discard_attack(all_energy=True)
from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card


def _fire_energy(card):
    return is_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


card = PokemonCardDef(
    guid="172ada85-c2bd-5a4c-a4fa-dcbbb765688b",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic"],
    subtypes=["Basic"],
    collector_number=248,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Overflowing Flame",
            game_text="Search your deck for up to 3 [R] Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=su.search_to_hand(_fire_energy, count=3, reveal=True, prompt="Choose up to 3 [R] Energy cards."),
        ),
        Attack(
            title="Flare Shot",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
            effect=_discard_all,
        ),
    ],
)
