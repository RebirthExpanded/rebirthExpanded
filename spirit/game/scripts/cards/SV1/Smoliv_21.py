"""Smoliv (SV1 21 -- JP SV1S 006; English PAF/102, SVI/21, SVP/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def nutrients(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 30 damage from")
        if target is not None:
            await ctx.heal(30, target)


card = PokemonCardDef(
    guid="4ff59110-0191-5891-846b-8b01fc8f4147",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    display_name="Smoliv",
    searchable_by=["Smoliv", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=928,
    abilities=[
        Attack(
            title="Nutrients",
            game_text="Heal 30 damage from 1 of your Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=nutrients,
        ),
        Attack(
            title="Spray Fluid",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
