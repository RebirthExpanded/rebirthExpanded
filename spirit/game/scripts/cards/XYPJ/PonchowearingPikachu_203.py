"""Poncho-wearing Pikachu (XYPJ 203 -- JP XYP 203; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.data_utils import subtypes_for
from spirit.game.session.effects import is_pokemon_card


def _mega(card):
    return is_pokemon_card(card) and any(s in ("MEGA", "SV_Mega") for s in subtypes_for(card.archetype_id))


async def _mega_pretend(ctx):
    """Flip a coin. If heads, search your deck for a Mega Evolution Pokemon,
    reveal it, and put it into your hand. Then, shuffle your deck."""
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if results and results[0]:
        await su.search_to_hand(_mega, count=1, reveal=True,
                                prompt="Choose a Mega Evolution Pokémon to put into your hand.")(ctx)


card = PokemonCardDef(
    guid="1a0cce8c-c95b-507b-a928-ea266cb2e602",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PonchowearingPikachu.Name",
    display_name="Poncho-wearing Pikachu",
    searchable_by=["Poncho-wearing Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=203,
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
            title="Mega Pretend",
            game_text="Flip a coin. If heads, search your deck for a Mega Evolution Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_mega_pretend,
        ),
        Attack(
            title="Triple Spark",
            game_text="Flip 3 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=30),
        ),
    ],
)
