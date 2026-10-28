"""Capsakid (SV1 28 -- JP SV1V 013; English PAF/106, SVI/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


card = PokemonCardDef(
    guid="4397c519-4f22-56b3-9391-a76c78029f0b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    display_name="Capsakid",
    searchable_by=["Capsakid", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=951,
    abilities=[
        Attack(
            title="Increasing Spice",
            game_text="Search your deck for a Basic Fire Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_fire, count=1, to_self=True, prompt="Choose a Basic Fire Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Playful Kick",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
