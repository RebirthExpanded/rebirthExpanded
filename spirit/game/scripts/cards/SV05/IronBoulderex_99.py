"""Iron Boulder ex (SV05 99 -- JP SV5M 041; English SVP/147, TEF/192, TEF/207, TEF/217, TEF/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class RepulsorAxePassive(Passive):
    """Damaged by an attack next turn: 8 damage counters on the Attacking Pokemon."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if calc.is_attack and calc.is_opposing and calc.amount > 0 and target is carrier and calc.attacker is not None:
            await ctx.deal_damage(80, target=calc.attacker, apply_modifiers=False, as_counters=True)
        return None


async def repulsor_axe(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, RepulsorAxePassive())


card = PokemonCardDef(
    guid="1980f9e5-3fcb-5d04-8356-25a2727ebf10",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulderex.Name",
    display_name="Iron Boulder ex",
    searchable_by=["Iron Boulder ex", "Basic", "ex", "Future"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=99,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=1022,
    abilities=[
        Attack(
            title="Repulsor Axe",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=repulsor_axe,
        ),
        Attack(
            title="Power Stomp",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
