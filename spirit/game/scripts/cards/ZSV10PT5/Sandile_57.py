"""Sandile (ZSV10PT5 57 -- JP SV11B 060; English BLK/135, BLK/57). Japanese art.
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
    guid="500cdad6-e963-582c-a6a1-3b4fe15805e8",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=551,
    abilities=[
        Attack(
            title="Tighten Up",
            game_text="Your opponent discards a card from their hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=_tighten_up(1),
        ),
    ],
)
