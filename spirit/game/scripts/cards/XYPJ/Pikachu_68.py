"""Pikachu (XYPJ 68 -- JP XYP 068; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.data_utils import def_for
from spirit.game.session.effects import is_pokemon_card


def _pikachu(card):
    return is_pokemon_card(card) and getattr(def_for(card.archetype_id), "display_name", "") == "Pikachu"


async def _outbreak(ctx):
    """Flip 3 coins; bench up to that many Pikachu from the deck, then shuffle."""
    results = await ctx.flip_coins(3, ctx.ability.title if ctx.ability else "")
    heads = sum(1 for r in results if r)
    if heads:
        await su.search_to_bench(_pikachu, count=heads, prompt="Choose Pikachu to put onto your Bench.")(ctx)


card = PokemonCardDef(
    guid="a1bbc459-cd3c-539c-b60c-026beaa5aed0",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Outbreak!?",
            game_text="Flip 3 coins. For each heads, search your deck for a Pikachu and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=_outbreak,
        ),
    ],
)
