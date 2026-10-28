"""Probopass (SV3 146 -- JP SV3 079; English OBF/146). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="ccdbb871-6bd5-5275-86d5-2eb69f9755ee",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Triple Nose",
            game_text="Flip 3 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=40),
        ),
        Attack(
            title="Iron Buster",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_hit_then_lock,
        ),
    ],
)
