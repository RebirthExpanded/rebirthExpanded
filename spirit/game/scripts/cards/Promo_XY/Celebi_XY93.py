"""Celebi (XY Black Star Promos XY93).

Basic Grass Pokemon. HP 70, weakness Fire x2, retreat 1.

  Leap Through Time  (Ability)  When this Pokemon is Knocked Out, flip a
                                coin. If heads, shuffle this Pokemon and
                                all cards attached to it into your deck,
                                and your opponent can't take any Prize
                                cards for it.
  Sparkle Motion  [G]  Put 1 damage counter on each of your opponent's
                       Pokemon.

Triggers.ON_KNOCKED_OUT_REPLACEMENT: the engine runs the flip before the
Prizes are counted; heads (True) sends the whole stack into the deck,
shuffled, and no Prize is taken. An Ability lock stops it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def leap_through_time(ctx) -> bool:
    results = await ctx.flip_coins(1, "Leap Through Time")
    return bool(results and results[0])


card = PokemonCardDef(
    guid="3fe533d2-cbc3-5384-b0be-eba42cb313c4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Leap Through Time",
            game_text="When this Pokémon is Knocked Out, flip a coin. If heads, shuffle this Pokémon and all cards attached to it into your deck, and your opponent can't take any Prize cards for it.",
            trigger=Triggers.ON_KNOCKED_OUT_REPLACEMENT,
            effect=leap_through_time,
        ),
        Attack(
            title="Sparkle Motion",
            game_text="Put 1 damage counter on each of your opponent's Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=place_counters(1, "each_opponent"),
        ),
    ],
)
