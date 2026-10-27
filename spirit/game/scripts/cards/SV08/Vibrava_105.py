"""Vibrava (SV08 105 -- JP SV7a 026; English SSP/105, SSP/206). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _TakesMore(Passive):
    def __init__(self, amount):
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target:
            calc.amount += self.amount


async def screech(ctx):
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_own_next_turn(d, _TakesMore(50))


card = PokemonCardDef(
    guid="748a0348-b1da-5abb-8e11-27ee11fa8319",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava",
    searchable_by=["Vibrava", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=328,
    abilities=[
        Attack(
            title="Screech",
            game_text="During your next turn, the Defending Pokémon takes 50 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=screech,
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
