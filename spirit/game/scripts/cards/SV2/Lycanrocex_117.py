"""Lycanroc ex (SV2 117 -- JP SV1a 050; English PAL/117, PAL/241). Japanese art.
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
    guid="edf0614a-48e0-57ec-b765-240dc553ee27",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanrocex.Name",
    display_name="Lycanroc ex",
    searchable_by=["Lycanroc ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=117,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Rock Throw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Scary Fangs",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 10 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=_reflect_after_hit(10),
        ),
    ],
)
