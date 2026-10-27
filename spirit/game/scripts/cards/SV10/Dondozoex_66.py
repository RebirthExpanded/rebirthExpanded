"""Dondozo ex (SV10 66 -- JP SV9a 032; English DRI/211, DRI/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0


async def dynamic_dive(ctx):
    if await ctx.ask_yes_no("Do 120 more damage? (This Pokémon also does 50 damage to itself.)"):
        await ctx.deal_damage(240)
        await ctx.deal_damage(50, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(120)


card = PokemonCardDef(
    guid="7475bfd7-69f7-5311-9b8c-7b996099a306",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozoex.Name",
    display_name="Dondozo ex",
    searchable_by=["Dondozo ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=66,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=977,
    abilities=[
        Attack(
            title="Avenging Billow",
            game_text="This attack does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(_own, 10, base=30),
        ),
        Attack(
            title="Dynamic Dive",
            game_text="You may do 120 more damage. If you do, this Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=dynamic_dive,
        ),
    ],
)
