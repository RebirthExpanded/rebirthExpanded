"""Hearthflame Mask Ogerpon ex (SV085 17 -- JP SV6 022; English PRE/148, PRE/17, TWM/192, TWM/212, TWM/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


async def dynamic_blaze(ctx):
    if _evolved_defender(ctx):
        await ctx.deal_damage(280)
        pool = list(ctx.attached_energies(ctx.attacker))
        if pool:
            await ctx.discard_cards(pool)
    else:
        await ctx.deal_damage(140)


card = PokemonCardDef(
    guid="07a72eba-2031-5e8a-bf18-0eb78505f7b2",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HearthflameMaskOgerponex.Name",
    display_name="Hearthflame Mask Ogerpon ex",
    searchable_by=["Hearthflame Mask Ogerpon ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=17,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1017,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Wrathful Hearth",
            game_text="This attack does 20 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_own, 20),
        ),
        Attack(
            title="Dynamic Blaze",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 140 more damage, and discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 3},
            damage=140,
            damage_operator="+",
            effect=dynamic_blaze,
        ),
    ],
)
