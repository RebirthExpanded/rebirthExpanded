from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def metal_slash(ctx):
    """70. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="aed8a866-f06a-5b4e-b222-b65d76f82ca5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetang.Name",
    display_name="Steven's Metang",
    searchable_by=["Steven's Metang", "Stage 1", "StevensMetang"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBeldum.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Metal Slash",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=metal_slash,
        ),
    ],
)
