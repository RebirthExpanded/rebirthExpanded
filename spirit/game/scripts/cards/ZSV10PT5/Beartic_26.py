"""Beartic (ZSV10PT5 26 -- JP SV11B 029; English BLK/110, BLK/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock_defender(ctx):
    await ctx.deal_damage()
    ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="4597254f-2189-5e45-b3f5-ec561ae1b0fb",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Continuous Headbutt",
            game_text="Flip a coin until you get tails. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=50),
        ),
        Attack(
            title="Sheer Cold",
            game_text="During your opponent's next turn, the Defending Pokémon can't use attacks.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=_hit_then_lock_defender,
        ),
    ],
)
