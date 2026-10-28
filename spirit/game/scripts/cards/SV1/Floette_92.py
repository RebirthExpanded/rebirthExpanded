"""Floette (SV1 92 -- JP SV1V 043; English SVI/92). Japanese art.
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
    guid="b8daf809-faba-5628-8c3c-ac90b8197384",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    display_name="Floette",
    searchable_by=["Floette", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    family_id=669,
    abilities=[
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 30 more damage, and heal 30 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=magical_leaf,
        ),
    ],
)
