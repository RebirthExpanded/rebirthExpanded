"""Krokorok (ZSV10PT5 58 -- JP SV11B 061; English BLK/136, BLK/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _tighten_up(n):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if hand:
            k = min(n, len(hand))
            await ctx.discard_from_hand(k, minimum=k, player_id=ctx.opponent_id,
                                        prompt=f"Discard {k} card(s) from your hand")
    return effect


card = PokemonCardDef(
    guid="22a95caa-e05b-5d9e-8f8b-ee5f34082738",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Tighten Up",
            game_text="Your opponent discards 2 cards from their hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_tighten_up(2),
        ),
    ],
)
