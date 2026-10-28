"""Wugtrio (SV1 57 -- JP SV1S 020; English PAF/122, PAF/224, SVI/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def undersea_tunnel(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Undersea Tunnel") if r)
    top = list(ctx.deck_top(3 * heads, player_id=ctx.opponent_id)) if heads else []
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="0a9088a8-a487-5a93-a8c7-1c6f78054008",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name",
    display_name="Wugtrio",
    searchable_by=["Wugtrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Undersea Tunnel",
            game_text="Flip 3 coins. For each heads, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=undersea_tunnel,
        ),
    ],
)
