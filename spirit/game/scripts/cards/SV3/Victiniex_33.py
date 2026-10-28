"""Victini ex (SV3 33 -- JP SVD 014; English OBF/33, SVP/142). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def strafe(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="173a853f-0ae6-5e7a-b5a2-438de338e438",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victiniex.Name",
    display_name="Victini ex",
    searchable_by=["Victini ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=33,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=strafe,
        ),
        Attack(
            title="Victory Flame",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=_hit_then_lock,
        ),
    ],
)
