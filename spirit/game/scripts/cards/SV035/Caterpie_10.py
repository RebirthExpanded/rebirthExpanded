"""Caterpie (SV035 10 -- JP SV2a 010; English MEW/10, MEW/172). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _grass(p) -> bool:
    return _of_type(p, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="a516fb1b-ba72-5b3d-99b2-461f2ab894ce",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    display_name="Caterpie",
    searchable_by=["Caterpie", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=10,
    abilities=[
        Attack(
            title="Leaf Munch",
            game_text="If your opponent's Active Pokémon is a Grass Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(ac.active_is(_grass), 30),
        ),
    ],
)
