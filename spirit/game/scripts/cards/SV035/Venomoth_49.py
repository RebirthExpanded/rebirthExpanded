"""Venomoth (SV035 49 -- JP SV2a 049; English MEW/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions

from spirit.game.session.effects import is_item_card


async def perplexing_powder(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="823cf57c-c347-5379-87e9-4d866c099511",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Perplexing Powder",
            game_text="Your opponent's Active Pokémon is now Confused. During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=perplexing_powder,
        ),
        Attack(
            title="Speed Wing",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
