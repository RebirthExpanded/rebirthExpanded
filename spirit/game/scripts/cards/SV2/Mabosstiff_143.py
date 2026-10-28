"""Mabosstiff (SV2 143 -- JP SV2P 049; English PAL/143). Japanese art.
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
    guid="3437b008-2709-5364-83f1-4fb3e132ee55",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=143,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Comeuppance",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_reflect_after_hit(),
        ),
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
