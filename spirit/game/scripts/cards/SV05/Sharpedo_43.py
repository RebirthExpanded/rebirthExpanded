"""Sharpedo (SV05 43 -- JP SV5K 017; English TEF/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def chew_off(ctx):
    await ctx.deal_damage()
    heads = sum(1 for r in await ctx.flip_coins(3, "Chew Off") if r)
    if heads:
        await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=heads)


card = PokemonCardDef(
    guid="65866b4f-b779-51c9-bf16-00a4fa6fbb10",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Chew Off",
            game_text="Flip 3 coins. For each heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=chew_off,
        ),
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
