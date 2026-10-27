"""Talonflame (ME3 14 -- JP M3 014; English POR/14, POR/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def sky_hunt(ctx):
    results = await ctx.flip_coins(1, "Sky Hunt")
    if results and results[0] and ctx.hand(ctx.opponent_id):
        await ac.discard_random_from_hand(ctx, ctx.opponent_id)


card = PokemonCardDef(
    guid="9117d0e9-a682-533a-8b51-9cd7f51096b1",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Sky Hunt",
            game_text="Once during your turn, you may use this Ability. Flip a coin. If heads, discard a random card from your opponent's hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=sky_hunt,
        ),
        Attack(
            title="Fire Wing",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=110,
        ),
    ],
)
