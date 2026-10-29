"""Radiant Eevee (Promo_SWSH 230 -- JP S10b 055; English SP/230). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _types_in_play(ctx) -> int:
    seen = set()
    for p in ctx.my_pokemon_in_play():
        seen.update(p.get_attribute(AttrID.POKEMON_TYPES) or [])
    return len(seen)


async def _twinkle_gathering(ctx):
    n = _types_in_play(ctx)
    if n <= 0:
        return
    picks = await ctx.search_deck(None, count=n, minimum=0,
                                  prompt=f"Choose up to {n} cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="fcf17714-d900-5bdf-9cec-c57aeda4b490",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantEevee.Name",
    display_name="Radiant Eevee",
    searchable_by=["Radiant Eevee", "Basic", "Radiant"],
    subtypes=["Basic", "Radiant"],
    collector_number=230,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareRadiant,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Twinkle Gathering",
            game_text="Search your deck for a number of cards up to the number of different types of Pokémon you have in play and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_twinkle_gathering,
        ),
        Attack(
            title="Boost Dash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
