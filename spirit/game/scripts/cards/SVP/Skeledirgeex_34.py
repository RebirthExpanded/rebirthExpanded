"""Skeledirge ex (SVP 34 -- JP SV1a 020; English PAL/233, PAL/258, PAL/272, PAL/37, SVP/34, SVP/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def vitality_song(ctx):
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(30, p)


async def burning_voice(ctx):
    amount = max(0, 270 - 10 * _counters(ctx.board, ctx.attacker))
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="289fa4d6-eb77-52c5-8191-988825ba4615",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirgeex.Name",
    display_name="Skeledirge ex",
    searchable_by=["Skeledirge ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=34,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Vitality Song",
            game_text="Heal 30 damage from each of your Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=vitality_song,
        ),
        Attack(
            title="Burning Voice",
            game_text="This attack does 10 less damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=270,
            damage_operator="-",
            effect=burning_voice,
        ),
    ],
)
