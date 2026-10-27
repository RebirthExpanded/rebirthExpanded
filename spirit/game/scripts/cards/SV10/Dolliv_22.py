"""Dolliv (SV10 22 -- JP MC 070; English DRI/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def nutrients(ctx):
    damaged = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose 1 of your Pokémon to heal 40 damage from")
    if target is not None:
        await ctx.heal(40, target)


card = PokemonCardDef(
    guid="ebebd287-49ec-58e0-a5f9-9dc6350c69de",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    display_name="Dolliv",
    searchable_by=["Dolliv", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Nutrients",
            game_text="Heal 40 damage from 1 of your Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=nutrients,
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
