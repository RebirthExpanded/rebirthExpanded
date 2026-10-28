"""Cetitan (SV1 60 -- JP SV1V 025; English SVI/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def sweeping_tackle(ctx):
    amount = max(0, 200 - 20 * _counters(ctx.board, ctx.attacker))
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="7701f943-3e73-5c0f-936e-a8a5e90d0942",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Sweeping Tackle",
            game_text="This attack does 20 less damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            damage_operator="-",
            effect=sweeping_tackle,
        ),
    ],
)
