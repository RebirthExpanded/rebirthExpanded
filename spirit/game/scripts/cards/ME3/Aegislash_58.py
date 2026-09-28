from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def metal_slash(ctx):
    """230. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="e946f5fb-6680-5b22-8108-df5b79beb29d",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=58,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Metal Slash",
            game_text="During your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=230,
            effect=metal_slash,
        ),
    ],
)
