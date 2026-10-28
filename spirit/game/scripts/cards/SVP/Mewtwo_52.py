"""Mewtwo (SVP 52 -- JP SV2a 150; English MEW/150, SVP/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class _Reflect(Passive):
    """During the opponent's next turn: damaged by an attack -> counters on
    the Attacking Pokemon (fixed amount, or the damage done when None)."""

    def __init__(self, counters=None):
        self.counters = counters

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if calc.is_attack and calc.is_opposing and calc.amount > 0 and target is carrier and calc.attacker is not None:
            amount = calc.amount if self.counters is None else 10 * self.counters
            await ctx.deal_damage(amount, target=calc.attacker, apply_modifiers=False, as_counters=True)
        return None


def _reflect_after_hit(counters=None):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(ctx.attacker, _Reflect(counters))
    return effect


card = PokemonCardDef(
    guid="943abf4b-594e-5925-8e0d-d2999fe227a0",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=150,
    abilities=[
        Attack(
            title="Reflective Barrier",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_reflect_after_hit(),
        ),
        Attack(
            title="Psyslash",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
