"""Roggenrola (RSV10PT5 46 -- JP SV11W 043; English WHT/127, WHT/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _HardenShield(Passive):
    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target and calc.amount <= 40:
            calc.amount = 0


async def harden(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, _HardenShield())


card = PokemonCardDef(
    guid="7d3075fe-2434-50f1-973d-2a6cb1276fe7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks if that damage is 40 or less.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=harden,
        ),
        Attack(
            title="Rolling Rocks",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
