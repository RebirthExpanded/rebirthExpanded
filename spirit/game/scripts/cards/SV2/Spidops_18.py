"""Spidops (SV2 18 -- JP SV2D 009; English PAL/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def entangling_trap(ctx):
    mine = ctx.attacker
    theirs = ctx.opponent_active()
    await ctx.shuffle_into_deck(full_stack(mine), ctx.player_id)
    if theirs is not None and not ctx.effects_blocked(theirs):
        await ctx.shuffle_into_deck(full_stack(theirs), ctx.opponent_id)


card = PokemonCardDef(
    guid="01fe629a-bdb4-51b6-85d5-7d054a390ad0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spidops.Name",
    display_name="Spidops",
    searchable_by=["Spidops", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    family_id=917,
    abilities=[
        Attack(
            title="Entangling Trap",
            game_text="Shuffle each player's Active Pokémon and all attached cards into their deck. (You choose a new Active Pokémon first.)",
            cost={PokemonTypes.GRASS: 2},
            effect=entangling_trap,
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.GRASS: 3},
            damage=130,
        ),
    ],
)
