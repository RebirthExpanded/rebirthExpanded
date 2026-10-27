"""Centiskorch (ME1 30 -- JP M1S 013; English MEG/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _discard_opp_energy_for_heads(ctx, coins):
    heads = sum(1 for r in await ctx.flip_coins(coins, ctx.ability.title if ctx.ability else "") if r)
    target = ctx.opponent_active()
    if heads and target is not None and not ctx.effects_blocked(target) and ctx.attached_energies(target):
        n = min(heads, len(ctx.attached_energies(target)))
        await ctx.discard_energy_from(target, n, minimum=n,
                                      prompt=f"Choose {n} Energy to discard from your opponent's Active Pokémon")


async def coiling_crush(ctx):
    await ctx.deal_damage()
    await _discard_opp_energy_for_heads(ctx, 2)


card = PokemonCardDef(
    guid="581375ff-d7e3-5d36-a930-05ecbe734465",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Attack(
            title="Coiling Crush",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=coiling_crush,
        ),
        Attack(
            title="Heat Crawler",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
