"""Bouffalant (SV08 151 -- JP SV8 087; English SSP/151). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class ReadyToRamPassive(Passive):
    async def damage_interceptor(self, ctx, calc, target, carrier):
        if calc.is_attack and calc.is_opposing and calc.amount > 0 and target is carrier and calc.attacker is not None:
            await ctx.deal_damage(60, target=calc.attacker, apply_modifiers=False, as_counters=True)
        return None


async def ready_to_ram(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, ReadyToRamPassive())


card = PokemonCardDef(
    guid="07cf5690-8e0f-5d3f-a313-4b106f57703b",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Ready to Ram",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put 6 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=ready_to_ram,
        ),
        Attack(
            title="Smashing Headbutt",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
