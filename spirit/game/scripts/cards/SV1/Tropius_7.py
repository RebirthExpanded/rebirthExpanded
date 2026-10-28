"""Tropius (SV1 7 -- JP SVAM 003; English SVI/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def fresh_picked_fruit(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon to heal 60 damage from")
        if target is not None:
            await ctx.heal(60, target)


card = PokemonCardDef(
    guid="161ec42f-0f5d-5014-8075-26aa20052f26",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Fresh-Picked Fruit",
            game_text="Heal 60 damage from 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=fresh_picked_fruit,
        ),
        Attack(
            title="Razor Leaf",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
