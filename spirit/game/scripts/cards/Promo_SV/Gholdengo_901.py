"""Gholdengo (JP "30th CELEBRATION" M6a 087 -- a Champions League 2027
commemorative card, not tournament-legal in Japan; no English print,
pool slot Promo_SV 901).

Stage 1 Metal Pokemon, evolves from Gimmighoul. HP 130, weakness Fire x2,
resistance Grass -30, retreat 2.

  Celebrate  [M]  If you have exactly 30 cards in your hand, take 2 Prize
                  cards. Then, shuffle your hand into your deck.
  Triple Smash  [M] 50x  Flip 3 coins. This attack does 50 damage for each
                         heads.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import Attack, PokemonCardDef


async def celebrate(ctx):
    if len(ctx.hand()) == 30:
        await ctx.take_prizes(2)
    await ctx.shuffle_into_deck(list(ctx.hand()), ctx.player_id)


card = PokemonCardDef(
    guid="1a90bb5e-95a7-5e4d-a791-ba39b280bc4b",
    key="Promo_SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name",
    display_name="Gholdengo",
    searchable_by=["Gholdengo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=901,
    set_code="Promo_SV",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Attack(title="Celebrate",
               game_text="If you have exactly 30 cards in your hand, take 2 Prize cards. Then, shuffle your hand into your deck.",
               cost={PokemonTypes.METAL: 1}, damage=0, effect=celebrate),
        Attack(title="Triple Smash", game_text="Flip 3 coins. This attack does 50 damage for each heads.",
               cost={PokemonTypes.METAL: 1}, damage=50, effect=flip_damage(coins=3, per_heads=50)),
    ],
)
