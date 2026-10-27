"""Glimmora (SV08 115 -- JP SV8 068; English SSP/115). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def corrosive_shards(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts:
        return
    await ctx.apply_special_condition(d, SpecialConditions.POISONED)
    if not ctx.effects_blocked(d):
        ctx.restrict_attachments(d)


card = PokemonCardDef(
    guid="5243e8e2-988e-5f89-b599-c49ee66acdb9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmora.Name",
    display_name="Glimmora",
    searchable_by=["Glimmora", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Attack(
            title="Corrosive Shards",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, Energy cards can't be attached from your opponent's hand to that Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=corrosive_shards,
        ),
        Attack(
            title="Rock Throw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
