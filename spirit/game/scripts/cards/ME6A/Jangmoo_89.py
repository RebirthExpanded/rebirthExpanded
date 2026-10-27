"""Jangmo-o (ME6A 89 -- JP M6a 089; English 30C/110). Japanese art.
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
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and defender not in ctx.knockouts and not ctx.effects_blocked(defender):
        ctx.add_passive_through_own_next_turn(defender, _TakesMore(30))


card = PokemonCardDef(
    guid="ce9aaafa-02e7-5da5-b944-a5c3259fd1be",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    display_name="Jangmo-o",
    searchable_by=["Jangmo-o", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=782,
    abilities=[
        Attack(
            title="Screech",
            game_text="During your next turn, the Defending Pokémon takes 30 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=screech,
        ),
        Attack(
            title="Dragon Claw",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
    ],
)
