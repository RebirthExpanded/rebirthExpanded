"""Hearthflame Mask Ogerpon (SV10 44 -- JP SV9a 021; English DRI/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="61e51c4e-ee83-52fc-a885-dc4a759ebcbe",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HearthflameMaskOgerpon.Name",
    display_name="Hearthflame Mask Ogerpon",
    searchable_by=["Hearthflame Mask Ogerpon", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1017,
    abilities=[
        Attack(
            title="Fire Kagura",
            game_text="Search your deck for a Basic Fire Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_fire, count=1, prompt="Choose a Basic Fire Energy card to attach to 1 of your Pokémon."),
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
