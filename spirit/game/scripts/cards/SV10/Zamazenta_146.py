"""Zamazenta (SV10 146 -- JP SV10 075; English DRI/146, DRI/201). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class StrongBashPassive(Passive):
    """Reflects the damage this Pokemon takes onto the attacker as counters."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


async def strong_bash(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, StrongBashPassive())


card = PokemonCardDef(
    guid="3bd29e49-cfcc-5e83-8ff3-48515547e17b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=889,
    abilities=[
        Attack(
            title="Strong Bash",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=strong_bash,
        ),
    ],
)
