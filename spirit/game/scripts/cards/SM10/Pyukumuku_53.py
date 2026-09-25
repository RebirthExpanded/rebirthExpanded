"""Pyukumuku (SM - Unbroken Bonds 53/214 -- JP SM9b 013/054).

Basic Water Pokemon. HP 70, weakness Grass x2, retreat 1.

  Call for Family  [C]        Search your deck for up to 2 Basic Pokemon and
                              put them onto your Bench. Then, shuffle your deck.
  Surprise Fist    [WCC] 60+  You and your opponent play Rock-Paper-Scissors.
                              If you win, this attack does 60 more damage.

Rock-Paper-Scissors is the shared helper (Mr. Mime SWSH11): a tie is
replayed until someone wins.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import rock_paper_scissors, search_to_bench
from spirit.game.data_utils import Attack, PokemonCardDef


async def surprise_fist(ctx):
    won = await rock_paper_scissors(ctx)
    await ctx.deal_damage(120 if won else 60)


card = PokemonCardDef(
    guid="ab4a937b-9b27-5faf-b983-e4d2133b27ce",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name",
    display_name="Pyukumuku",
    searchable_by=['Pyukumuku', 'Basic', 'Pyukumuku'],
    subtypes=['Basic'],
    collector_number=53,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=771,
    abilities=[
        Attack(title="Call for Family", game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=search_to_bench(count=2)),
        Attack(title="Surprise Fist", game_text="You and your opponent play Rock-Paper-Scissors. If you win, this attack does 60 more damage.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator="+",
               effect=surprise_fist),
    ],
)
