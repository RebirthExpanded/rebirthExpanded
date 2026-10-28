"""Growlithe (SV1 31 -- JP SVP 024; English SVI/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


card = PokemonCardDef(
    guid="0368a0fc-ea7a-548e-81fe-e12db1df406a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
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
