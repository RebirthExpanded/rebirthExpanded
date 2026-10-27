"""Liepard (RSV10PT5 56 -- JP SV11W 053; English WHT/137, WHT/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def knock_off(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="bd9098f6-2d10-5163-8884-f4ba27c7e16e",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=50,
            effect=knock_off,
        ),
    ],
)
