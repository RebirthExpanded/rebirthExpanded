"""Frogadier (SV3 57 -- JP SVD 028; English OBF/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def strafe(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="cd22b9ba-d0c5-5cfd-bf42-a4b2d7a2d7ca",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    display_name="Frogadier",
    searchable_by=["Frogadier", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=strafe,
        ),
    ],
)
