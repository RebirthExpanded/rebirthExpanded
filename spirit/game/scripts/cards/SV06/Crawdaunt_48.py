"""Crawdaunt (SV06 48 -- JP SV5a 020; English TWM/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def snip_snip(ctx):
    await ctx.deal_damage()
    heads = sum(1 for r in await ctx.flip_coins(2, "Snip Snip") if r)
    top = list(ctx.deck_top(heads, player_id=ctx.opponent_id)) if heads else []
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="5a7ac1f6-5cf6-56e6-a255-ba30fbcb759c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Attack(
            title="Snip Snip",
            game_text="Flip 2 coins. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=snip_snip,
        ),
        Attack(
            title="Rampaging Hammer",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=_hit_then_lock,
        ),
    ],
)
