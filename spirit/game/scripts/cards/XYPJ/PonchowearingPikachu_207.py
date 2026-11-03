"""Poncho-wearing Pikachu (XYPJ 207 -- JP XYP 207; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _wild_blaze(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if results and not results[0]:
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.player_id))


card = PokemonCardDef(
    guid="21f87869-38b7-55e8-9d99-987bee261ec5",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PonchowearingPikachu.Name",
    display_name="Poncho-wearing Pikachu",
    searchable_by=["Poncho-wearing Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=207,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Wild Blaze?",
            game_text="Flip a coin. If tails, discard the top 3 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=90,
            effect=_wild_blaze,
        ),
    ],
)
