"""Pawmot (ME2 34 -- JP M2 034; English PFL/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def voltaic_fist(ctx):
    boost = await ctx.ask_yes_no("Have this Pokémon also do 60 damage to itself and make your opponent's Active Pokémon Paralyzed?")
    await ctx.deal_damage()
    if boost:
        await ctx.deal_damage(60, target=ctx.attacker, apply_modifiers=False)
        target = ctx.opponent_active()
        if target is not None and target not in ctx.knockouts:
            await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="00cd742a-2750-5520-bbbc-f27102ddb1de",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Voltaic Fist",
            game_text="You may have this Pokémon also do 60 damage to itself and make your opponent's Active Pokémon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=130,
            effect=voltaic_fist,
        ),
    ],
)
