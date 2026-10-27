"""Floragato (SV09 17 -- JP SV9 011; English JTG/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def magical_leaf(ctx):
    results = await ctx.flip_coins(1, "Magical Leaf")
    heads = bool(results and results[0])
    await ctx.deal_damage(30 + (30 if heads else 0))
    if heads:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="b3fbde19-436f-5f66-a154-8f175bc82270",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    display_name="Floragato",
    searchable_by=["Floragato", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 30 more damage, and heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=magical_leaf,
        ),
    ],
)
