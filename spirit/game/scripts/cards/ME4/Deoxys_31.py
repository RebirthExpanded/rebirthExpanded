"""Deoxys (ME4 31 -- JP M4 031; English CRI/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)


card = PokemonCardDef(
    guid="ee8ae4d2-69f5-5e99-9711-21c6a95da510",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title="Genome Charge",
            game_text="Search your deck for up to 2 Basic Psychic Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_psychic, count=2, to_self=True, prompt="Choose up to 2 Basic Psychic Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 20, base=80),
        ),
    ],
)
