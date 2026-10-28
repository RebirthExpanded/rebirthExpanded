"""Beedrill (SV035 15 -- JP SV2a 015; English MEW/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def nadir_needle(ctx):
    empty = not ctx.hand()
    await ctx.deal_damage(150 if empty else 30)
    d = ctx.opponent_active()
    if empty and d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(d, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="299c3b84-26e7-53f4-811a-1b3b48de6653",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Nadir Needle",
            game_text="If you have no cards in your hand, this attack does 120 more damage, and your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=nadir_needle,
        ),
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=110,
        ),
    ],
)
