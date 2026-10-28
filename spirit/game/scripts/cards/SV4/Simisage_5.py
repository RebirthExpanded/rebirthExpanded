"""Simisage (SV4 5 -- JP SV4K 002; English PAR/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



class MonkeyTrioPassive(Passive):
    """Simisage, Simisear and Simipour in play: no [C] in attack costs."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or not cost.get("Colorless"):
            return cost
        names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in board.pokemon_in_play(pokemon.owning_player_id)}
        if {"Simisage", "Simisear", "Simipour"} <= names:
            cost = dict(cost)
            del cost["Colorless"]
        return cost
from spirit.game.session.passives import Passive, carrier_pokemon



def _has_ability(pokemon) -> bool:
    return any(isinstance(e, dict) and e.get("abilityType") not in (None, "Attack")
               for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or []))


class _ArmThrustShield(Passive):
    def prevents_damage(self, calc, carrier):
        a = calc.attacker
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target and a is not None
                    and _has_ability(a) and a.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) != "Simisage")


async def arm_thrust_needle(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _ArmThrustShield())


card = PokemonCardDef(
    guid="e9508f57-1e68-586b-a71f-14ea1adcda3d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    family_id=511,
    abilities=[
        Ability(
            title="Monkey Trio",
            game_text="If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.",
            passive=MonkeyTrioPassive(),
        ),
        Attack(
            title="Arm Thrust Needle",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Pokémon that have an Ability, except any Simisage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=arm_thrust_needle,
        ),
    ],
)
