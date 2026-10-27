"""Lilligant (SV09 7 -- JP SVM 008; English JTG/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _grass_or_fire(attacker) -> bool:
    return _of_type(attacker, PokemonTypes.GRASS) or _of_type(attacker, PokemonTypes.FIRE)


card = PokemonCardDef(
    guid="23e3ff2c-b401-5ee6-9d40-4bace680aa16",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Ability(
            title="Sunny Day",
            game_text="Attacks used by your Grass Pokémon and Fire Pokémon do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=pc.team_damage_boost_passive(20, attacker_pred=_grass_or_fire),
        ),
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
