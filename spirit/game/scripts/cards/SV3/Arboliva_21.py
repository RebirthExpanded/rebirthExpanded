"""Arboliva (SV3 21 -- JP SVD 011; English OBF/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def healing_fruit(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon to heal all damage from")
        if target is not None:
            await ctx.heal(10 * _counters(ctx.board, target), target)


card = PokemonCardDef(
    guid="83d5578f-ce96-5e9f-b790-06d6abd99454",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name",
    display_name="Arboliva",
    searchable_by=["Arboliva", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Healing Fruit",
            game_text="Heal all damage from 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=healing_fruit,
        ),
        Attack(
            title="Oil Shot",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=90,
        ),
    ],
)
