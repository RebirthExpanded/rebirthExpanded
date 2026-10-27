"""Tangrowth (SV06 2 -- JP SV5a 002; English TWM/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def loom_over(ctx):
    amount = max(0, 150 - 10 * _counters(ctx.board, ctx.attacker))
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="cfb0ba98-5e4d-5624-a5b3-0bd020340000",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Ability(
            title="Thicket Body",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Loom Over",
            game_text="This attack does 10 less damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            damage_operator="-",
            effect=loom_over,
        ),
    ],
)
