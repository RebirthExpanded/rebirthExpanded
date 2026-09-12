"""Durant (BW - Noble Victories 83/101 -- JP BW2-B 054/066, the art here).

Basic Metal Pokemon. HP 70, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Devour [M]  For each of your Durant in play, discard the top card of
              your opponent's deck.
  Vice Grip [CC] 30
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef, def_for


async def devour(ctx):
    durants = sum(1 for p in ctx.my_pokemon_in_play()
                  if (getattr(def_for(p.archetype_id), "display_name", "") or "") == "Durant")
    top = ctx.deck_top(durants, player_id=ctx.opponent_id)
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="05ffa3de-a63b-5e46-a793-206cb0fcf4bb",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=632,
    abilities=[
        Attack(title="Devour",
               game_text="For each of your Durant in play, discard the top card of your opponent's deck.",
               cost={PokemonTypes.METAL: 1}, effect=devour),
        Attack(title="Vice Grip", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=30),
    ],
)
