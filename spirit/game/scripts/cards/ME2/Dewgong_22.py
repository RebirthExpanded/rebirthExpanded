"""Dewgong (ME2 22 -- JP M2 022; English PFL/22, PFL/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])



def _fire_or_water(attacker) -> bool:
    return _of_type(attacker, PokemonTypes.FIRE) or _of_type(attacker, PokemonTypes.WATER)


card = PokemonCardDef(
    guid="9b8dbb71-c8ac-5c09-896d-d3d338a40256",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="This Pokémon takes 30 less damage from attacks from your opponent's Fire or Water Pokémon (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30, attacker_pred=_fire_or_water),
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=70),
        ),
    ],
)
