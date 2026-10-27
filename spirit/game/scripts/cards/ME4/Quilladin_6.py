"""Quilladin (ME4 6 -- JP M4 006; English CRI/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="2cb1cfa6-a6b4-5b01-9762-618140667a2b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    display_name="Quilladin",
    searchable_by=["Quilladin", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Leafy Charge",
            game_text="Search your deck for a Basic Grass Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=su.search_attach_energy(_basic_grass, count=1, to_self=True, prompt="Choose a Basic Grass Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Vine Whip",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
