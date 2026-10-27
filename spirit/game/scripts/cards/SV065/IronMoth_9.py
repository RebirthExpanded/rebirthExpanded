"""Iron Moth (SV065 9 -- JP SV6a 009; English SFA/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _leech(ctx):
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, ctx.attacker)
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class _ShieldFrom(Passive):
    """"Prevent all damage done to this Pokemon by attacks from <kind>"
    during the opponent's next turn."""

    def __init__(self, attacker_pred):
        self.attacker_pred = attacker_pred

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None and self.attacker_pred(calc.attacker))


def _shield_after_hit(attacker_pred):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(ctx.attacker, _ShieldFrom(attacker_pred))
        if ctx.attacker.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(ctx.attacker.entity_id)
    return effect
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


def _ancient(attacker) -> bool:
    return _has_sub(attacker, "Ancient")


card = PokemonCardDef(
    guid="4c661d0e-26b5-5614-903f-60166e4a6e7c",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name",
    display_name="Iron Moth",
    searchable_by=["Iron Moth", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=9,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=994,
    abilities=[
        Attack(
            title="Suction",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_leech,
        ),
        Attack(
            title="Anachronism Repulsor",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Ancient Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_shield_after_hit(_ancient),
        ),
    ],
)
