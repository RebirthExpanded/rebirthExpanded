"""Weavile (SV065 14 -- JP SV6a 014; English ASC/228, ASC/45, SFA/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def hail_claw(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    target = ctx.opponent_active()
    if target is not None and target not in ctx.knockouts:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="e1fba141-2ea5-5f85-9e87-6e1ff676c227",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Hail Claw",
            game_text="Discard all Energy from this Pokémon. Your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=hail_claw,
        ),
    ],
)
