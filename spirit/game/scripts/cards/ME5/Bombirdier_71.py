"""Bombirdier (ME5 71 -- JP M5 069; English PBL/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CardType
from spirit.game.session.passives import effective_bench_capacity


def _benchable(card) -> bool:
    # Any Pokemon card: an evolved one lands on the Bench as it is
    # (the Grimsley's Move Q&A).
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value


def _space(ctx) -> int:
    return effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())


async def challenging_delivery(ctx):
    results = await ctx.flip_coins(2, "Challenging Delivery")
    if len(results) == 2 and all(results):
        if _space(ctx) > 0:
            picks = await ctx.search_deck(_benchable, count=1, minimum=0,
                                          prompt="Choose a Pokémon to put onto your Bench.")
            for card in picks:
                await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="82002f42-1459-590d-bd53-9631d7711181",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=962,
    abilities=[
        Attack(
            title="Challenging Delivery",
            game_text="Flip 2 coins. If both of them are heads, search your deck for a Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=challenging_delivery,
        ),
        Attack(
            title="Speed Wing",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
