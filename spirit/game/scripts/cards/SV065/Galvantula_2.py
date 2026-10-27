"""Galvantula (SV065 2 -- JP SV6a 002; English SFA/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



def _has_ability(pokemon) -> bool:
    return any(isinstance(e, dict) and e.get("abilityType") not in (None, "Attack")
               for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or []))


class CompoundEyesPassive(Passive):
    """+50 to the opponent's Active Pokemon that has an Ability (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if (calc.is_attack and calc.attacker is me and calc.to_active and calc.is_opposing
                and _has_ability(calc.target)):
            calc.amount += 50


def _has_lightning(ctx) -> bool:
    return any(is_energy_of_type(e, PokemonTypes.LIGHTNING) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="10004dfd-d5f9-5f0e-84d0-ab56da567017",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Ability(
            title="Compound Eyes",
            game_text="Attacks used by this Pokémon do 50 more damage to your opponent's Active Pokémon that has an Ability (before applying Weakness and Resistance).",
            passive=CompoundEyesPassive(),
        ),
        Attack(
            title="Shocking Web",
            game_text="If this Pokémon has any Lightning Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_has_lightning, 80),
        ),
    ],
)
