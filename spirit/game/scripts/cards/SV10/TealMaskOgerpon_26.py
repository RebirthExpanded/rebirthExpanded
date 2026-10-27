"""Teal Mask Ogerpon (SV10 26 -- JP SV9a 012; English DRI/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="3e3fc52f-cbac-59f0-a91b-c63c01a38b6a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerpon.Name",
    display_name="Teal Mask Ogerpon",
    searchable_by=["Teal Mask Ogerpon", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1017,
    abilities=[
        Attack(
            title="Grass Kagura",
            game_text="Search your deck for a Basic Grass Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_grass, count=1, prompt="Choose a Basic Grass Energy card to attach to 1 of your Pokémon."),
        ),
        Attack(
            title="Ogre's Hammer",
            game_text="During your next turn, this Pokémon can't use Ogre's Hammer.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
