"""Quagsire V (SPJ 311 -- JP SP 311; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import PokemonTypes


def _has_fighting(ctx) -> bool:
    return any(is_energy_of_type(e, PokemonTypes.FIGHTING) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="c3af80b8-3ca7-509b-9ef4-21122453b2cf",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.QuagsireV.Name",
    display_name="Quagsire V",
    searchable_by=["Quagsire V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=311,
    set_code="SPJ",
    regulation_mark="F",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=195,
    abilities=[
        Ability(
            title="Unaware",
            game_text="Prevent all effects of attacks from your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=pc.attack_effect_shield_passive(),
        ),
        Attack(
            title="Mud Head",
            game_text="If this Pokémon has any [F] Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_has_fighting, 120),
        ),
    ],
)
