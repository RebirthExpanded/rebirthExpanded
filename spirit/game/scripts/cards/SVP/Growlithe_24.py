"""Growlithe (SVP 24 -- JP SV1V 015; English SVI/31, SVP/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


card = PokemonCardDef(
    guid="69b5f2b2-0e31-51b0-a31b-de96ba875aa3",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Stoke",
            game_text="Search your deck for up to 2 Basic Fire Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_fire, count=2, to_self=True, prompt="Choose up to 2 Basic Fire Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Fire Claws",
            game_text="",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
        ),
    ],
)
