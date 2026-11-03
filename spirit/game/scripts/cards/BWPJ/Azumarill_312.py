"""Azumarill (BWPJ 312 -- JP WAK 012; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su



def _flip_heal(amount):
    """Printed damage, then flip a coin: heads heals `amount` from this Pokemon."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
        if results and results[0]:
            await ctx.heal(amount, ctx.attacker)
    return effect


card = PokemonCardDef(
    guid="7c9559c1-c27a-52d3-a1ee-2a189627e497",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=312,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=298,
    abilities=[
        Attack(
            title="Bubble Drain",
            game_text="Flip a coin. If heads, heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_flip_heal(30),
        ),
    ],
)
