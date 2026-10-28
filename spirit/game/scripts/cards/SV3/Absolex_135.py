"""Absol ex (SV3 135 -- JP SV3 073; English OBF/135, OBF/214). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def future_sight(ctx):
    index = await ctx.choose("Look at the top 3 cards of which deck?", ["Your deck", "Your opponent's deck"])
    pid = ctx.opponent_id if index == 1 else ctx.player_id
    if ctx.deck_top(1, player_id=pid):
        await ctx.reorder_deck_top(3, player_id=pid, prompt="Rearrange the top cards")


def _small_hand(ctx) -> bool:
    return len(ctx.hand(ctx.opponent_id)) <= 3


card = PokemonCardDef(
    guid="4f3e2c8c-759c-5b9a-bdfe-e0e7864a08a3",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absolex.Name",
    display_name="Absol ex",
    searchable_by=["Absol ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=135,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=359,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 3 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=future_sight,
        ),
        Attack(
            title="Cursed Slug",
            game_text="If your opponent has 3 or fewer cards in their hand, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_small_hand, 120),
        ),
    ],
)
