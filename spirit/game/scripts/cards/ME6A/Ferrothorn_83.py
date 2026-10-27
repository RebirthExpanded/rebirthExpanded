"""Ferrothorn (ME6A 83 -- JP M6a 083; English 30C/104). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def kaboom_needles(ctx):
    await ac.damage_all_opponents(50)(ctx)
    await ctx.deal_damage(130, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="6f20d94e-1284-5a92-8ac3-da25905142ef",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Attack(
            title="Spike Sting",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Kaboom Needles",
            game_text="This attack does 50 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) This Pokémon also does 130 damage to itself.",
            cost={PokemonTypes.METAL: 2},
            effect=kaboom_needles,
        ),
    ],
)
