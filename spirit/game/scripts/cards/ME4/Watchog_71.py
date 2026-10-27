"""Watchog (ME4 71 -- JP M4 069; English CRI/71, CRI/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def snap_inspection(ctx):
    results = await ctx.flip_coins(3, "Snap Inspection")
    heads = sum(1 for r in results if r)
    hand = ctx.hand(ctx.opponent_id)
    if not heads or not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    picks = await ctx.choose_cards(hand, min(heads, len(hand)), minimum=min(heads, len(hand)),
                                   prompt="Choose cards to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="edd93090-7341-5df4-98c2-96427e632f4b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Snap Inspection",
            game_text="Flip 3 coins. If any of them are heads, your opponent reveals their hand. For each heads, choose a card you find there and shuffle it into your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snap_inspection,
        ),
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
