"""Floatzel (SV3 49 -- JP SV1a 026; English OBF/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def swirling_tail(ctx):
    results = await ctx.flip_coins(1, "Swirling Tail")
    d = ctx.opponent_active()
    if results and results[0] and d is not None and not ctx.effects_blocked(d):
        await ctx.put_in_hand(full_stack(d), reveal=False)


card = PokemonCardDef(
    guid="dc7ad1c3-dba5-56c2-bd42-3a6b007d60ab",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name",
    display_name="Floatzel",
    searchable_by=["Floatzel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title="Swirling Tail",
            game_text="Flip a coin. If heads, put your opponent's Active Pokémon and all attached cards into your opponent's hand.",
            cost={PokemonTypes.WATER: 1},
            effect=swirling_tail,
        ),
        Attack(
            title="Waterfall",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
