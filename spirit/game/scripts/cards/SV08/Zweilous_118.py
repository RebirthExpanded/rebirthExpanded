"""Zweilous (SV - Surging Sparks 118/191 -- JP SV8 071/106, the art here).

Stage 1 Darkness Pokemon (evolves from Deino). HP 100, weakness Grass
x2, retreat 2.

  Stomp Off  [D]    Discard the top 2 cards of your opponent's deck.
  Dark Fang  [DCC] 60
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

MILL = 2


async def stomp_off(ctx):
    await ctx.discard_cards(ctx.deck_top(MILL, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="03fb572a-e0b5-5dd1-9ad7-4125de8ae15f",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Stomp Off",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=stomp_off,
        ),
        Attack(
            title="Dark Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
