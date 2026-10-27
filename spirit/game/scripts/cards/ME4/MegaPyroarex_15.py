"""Mega Pyroar ex (ME4 15 -- JP M4 015; English CRI/15, CRI/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def fiery_big_bang(ctx):
    await ctx.deal_damage(max(0, 290 - 10 * _counters(ctx.board, ctx.attacker)))


card = PokemonCardDef(
    guid="40787d23-68d8-5f27-b141-0a0873fbff69",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaPyroarex.Name",
    display_name="Mega Pyroar ex",
    searchable_by=["Mega Pyroar ex", "Stage 1", "ex", "SV_Mega"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=15,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Attack(
            title="Ferocious Bellow",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=pc.debuff_defender_attacks(50),
        ),
        Attack(
            title="Fiery Big Bang",
            game_text="This attack does 10 less damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=290,
            damage_operator="-",
            effect=fiery_big_bang,
        ),
    ],
)
