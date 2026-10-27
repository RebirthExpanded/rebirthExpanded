"""Gurdurr (SV06 104 -- JP SV6 060; English TWM/104). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def superpower(ctx):
    if await ctx.ask_yes_no("Do 30 more damage? (This Pokémon also does 30 damage to itself.)"):
        await ctx.deal_damage(80)
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(50)


card = PokemonCardDef(
    guid="a8bfd4ad-2e96-5536-842c-8d69b6b46770",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    display_name="Gurdurr",
    searchable_by=["Gurdurr", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Knuckle Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Superpower",
            game_text="You may do 30 more damage. If you do, this Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=superpower,
        ),
    ],
)
