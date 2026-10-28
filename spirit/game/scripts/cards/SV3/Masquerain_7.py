"""Masquerain (SV3 7 -- JP SV2P 002; English OBF/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def panic_prompting_pattern(ctx):
    heads = await ctx.flip_until_tails("Panic-Prompting Pattern")
    if heads:
        await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=heads)


card = PokemonCardDef(
    guid="2f92f2b8-9169-5c6e-8258-b4c0ecafc47a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Panic-Prompting Pattern",
            game_text="Flip a coin until you get tails. For each heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=panic_prompting_pattern,
        ),
        Attack(
            title="Bug Buzz",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
