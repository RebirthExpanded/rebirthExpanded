"""Krookodile (ZSV10PT5 59 -- JP SV11B 062; English BLK/137, BLK/59). Japanese art.
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
from spirit.game.card_effects import attacks_common as ac


def _small_hand(ctx) -> bool:
    return len(ctx.hand(ctx.opponent_id)) <= 3


card = PokemonCardDef(
    guid="0e2e8980-b3a7-55a2-83ee-a808250186a6",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Tighten Up",
            game_text="Your opponent discards 2 cards from their hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=_tighten_up(2),
        ),
        Attack(
            title="Cursed Slug",
            game_text="If your opponent has 3 or fewer cards in their hand, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(_small_hand, 120),
        ),
    ],
)
