"""Palafin (SV05 49 -- JP SV5K 023; English TEF/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def vanguard_punch(ctx):
    n = _counters(ctx.board, ctx.attacker)
    await ctx.deal_damage()
    if n:
        await ctx.deal_damage(10 * n, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="2efb7d3b-df66-55ad-8b68-1a250a393f50",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Vanguard Punch",
            game_text="This Pokémon also does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.WATER: 1},
            damage=130,
            effect=vanguard_punch,
        ),
        Attack(
            title="Double Hit",
            game_text="Flip 2 coins. This attack does 90 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=90),
        ),
    ],
)
