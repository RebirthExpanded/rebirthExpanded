"""Greninja ex (ME6A 15 -- JP M6a 015; English 30C/148, 30C/21, MEP/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def stealthy_slash(ctx):
    pool = list(ctx.opponent_pokemon_in_play())
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    n = _counters(ctx.board, target)
    if n:
        await ctx.deal_damage(30 * n, target=target)


card = PokemonCardDef(
    guid="df4ce4d1-0a6a-5d4a-8e49-dedf9d2712a2",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=15,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Stealthy Slash",
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon for each damage counter on that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=stealthy_slash,
        ),
        Attack(
            title="Aqua Edge",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=160,
        ),
    ],
)
