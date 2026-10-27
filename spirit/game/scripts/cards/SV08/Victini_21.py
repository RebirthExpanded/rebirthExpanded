"""Victini (SV08 21 -- JP SV8 012; English SSP/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_evolution_pokemon


def _evo_fire(p) -> bool:
    return is_evolution_pokemon(p) and _of_type(p, PokemonTypes.FIRE)


card = PokemonCardDef(
    guid="fd6060b7-d486-5b19-bc0b-244020282030",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Ability(
            title="Victory Cheer",
            game_text="Attacks used by your Evolution Fire Pokémon do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=pc.team_damage_boost_passive(10, attacker_pred=_evo_fire),
        ),
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
