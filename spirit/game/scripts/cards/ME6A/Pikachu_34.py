"""Pikachu (ME6A 34 -- JP M6a 034; English 30C/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _WeakToLightning(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target is carrier_pokemon(carrier):
            calc.weak_types = [PokemonTypes.LIGHTNING.value]
            calc.weakness_applies = True
            calc.weakness_multiplier = 2


async def overwriting_bolt(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and defender not in ctx.knockouts and not ctx.effects_blocked(defender):
        ctx.add_passive_through_own_next_turn(defender, _WeakToLightning())


card = PokemonCardDef(
    guid="58a66571-6ba9-5369-a7f3-4b5cf3d3e3a0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Overwriting Bolt",
            game_text="The Defending Pokémon's Weakness is now Lightning until the end of your next turn. (Apply Weakness as x2.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=overwriting_bolt,
        ),
    ],
)
