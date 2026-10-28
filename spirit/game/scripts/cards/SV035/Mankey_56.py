"""Mankey (SV035 56 -- JP SV2a 056; English MEW/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def thrash(ctx):
    results = await ctx.flip_coins(1, "Thrash")
    if results and results[0]:
        await ctx.deal_damage(40)
    else:
        await ctx.deal_damage(20)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="c3c9490a-ac2c-559e-b3bf-b36ced3da974",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Thrash",
            game_text="Flip a coin. If tails, this Pokémon also does 20 damage to itself. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=thrash,
        ),
    ],
)
