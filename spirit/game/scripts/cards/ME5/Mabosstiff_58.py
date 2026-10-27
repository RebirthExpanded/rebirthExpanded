"""Mabosstiff (ME5 58 -- JP M5 056; English PBL/58). Japanese art.
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


async def plunging_headbutt(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _TakesMore(100))


card = PokemonCardDef(
    guid="9695a4f8-8955-5fa6-a590-46ede99b297f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
        Attack(
            title="Plunging Headbutt",
            game_text="During your opponent's next turn, this Pokémon takes 100 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 3},
            damage=210,
            effect=plunging_headbutt,
        ),
    ],
)
