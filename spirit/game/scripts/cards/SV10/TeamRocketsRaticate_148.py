"""Team Rocket's Raticate (SV10 148 -- JP SV10 108; English DRI/148, DRI/202). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def reckless_abandon(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Reckless Abandon")
    if results and not any(results):
        await ctx.deal_damage(90, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="b7aa57f0-85fc-5215-9d57-2dcc9257fea1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsRaticate.Name",
    display_name="Team Rocket's Raticate",
    searchable_by=["Team Rocket's Raticate", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Reckless Abandon",
            game_text="Flip 2 coins. If both of them are tails, this Pokémon also does 90 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=reckless_abandon,
        ),
    ],
)
