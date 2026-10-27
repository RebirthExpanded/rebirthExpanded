"""Stunfisk (ME2PT5 62 -- JP M2a 050; English ASC/62). Japanese art.
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


async def pouncing_trap(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or target in ctx.knockouts or ctx.effects_blocked(target):
        return
    import spirit.game.card_effects.attacks_common as _ac
    await _ac.condition_attack(no_retreat=True, damage=0)(ctx)
    ctx.add_passive_through_own_next_turn(target, _TakesMore(100))


card = PokemonCardDef(
    guid="0745ef01-55ea-5fc2-90a8-2b3d14d291ca",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=618,
    abilities=[
        Attack(
            title="Pouncing Trap",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat. During your next turn, the Defending Pokémon takes 100 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=pouncing_trap,
        ),
    ],
)
