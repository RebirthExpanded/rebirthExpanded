"""Deino (SV - Surging Sparks 117/191 -- JP SV8 070/106, the art here).

Basic Darkness Pokemon. HP 70, weakness Grass x2, retreat 1.

  Stomp Off  [D]   Discard the top card of your opponent's deck.
  Bite       [DC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

MILL = 1


async def stomp_off(ctx):
    await ctx.discard_cards(ctx.deck_top(MILL, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="11ded11a-18ad-54c6-a439-4d88d3bb48d5",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    display_name="Deino",
    searchable_by=["Deino", "Basic"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=633,
    abilities=[
        Attack(
            title="Stomp Off",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=stomp_off,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
