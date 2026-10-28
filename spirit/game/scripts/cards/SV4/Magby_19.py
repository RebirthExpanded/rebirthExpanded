"""Magby (SV4 19 -- JP SV4K 010; English PAR/186, PAR/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _ScorchingHeater(Passive):
    async def damage_interceptor(self, ctx, calc, target, carrier):
        if calc.is_attack and calc.is_opposing and calc.amount > 0 and target is carrier and calc.attacker is not None:
            await ctx.deal_damage(60, target=calc.attacker, apply_modifiers=False, as_counters=True)
        return None


async def scorching_heater(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, _ScorchingHeater())


card = PokemonCardDef(
    guid="ea506384-b6c4-5780-b3e1-5707333a5b9e",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Attack(
            title="Scorching Heater",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 6 damage counters on the Attacking Pokémon.",
            cost={},
            effect=scorching_heater,
        ),
    ],
)
