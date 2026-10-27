"""Heatran (ME5 7 -- JP M5 007; English PBL/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class _ShieldFrom(Passive):
    """"Prevent all damage done to this Pokemon by attacks from <kind>"
    during the opponent's next turn."""

    def __init__(self, attacker_pred):
        self.attacker_pred = attacker_pred

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None and self.attacker_pred(calc.attacker))


def _shield_after_hit(attacker_pred):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(ctx.attacker, _ShieldFrom(attacker_pred))
        if ctx.attacker.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(ctx.attacker.entity_id)
    return effect
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import SpecialConditions


def _has_condition(pokemon, *conditions) -> bool:
    have = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [] if pokemon is not None else []
    return any(CLIENT_SPECIAL_CONDITION_NAMES[c] in have for c in conditions)


def _burned(pokemon) -> bool:
    return _has_condition(pokemon, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="0e7e3bc2-83af-5149-9457-bc85d6defd50",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Lava Wall",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Burned Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_shield_after_hit(_burned),
        ),
    ],
)
