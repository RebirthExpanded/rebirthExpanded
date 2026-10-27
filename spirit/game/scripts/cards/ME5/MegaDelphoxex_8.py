"""Mega Delphox ex (ME5 8 -- JP MP 096; English PBL/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import AttrID, CardType
from spirit.game.session.passives import effective_bench_capacity


def _benchable(card) -> bool:
    # Any Pokemon card: an evolved one lands on the Bench as it is
    # (the Grimsley's Move Q&A).
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value


def _space(ctx) -> int:
    return effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())


async def trick_portal(ctx):
    top = ctx.deck_top(9)
    if not top:
        return
    pool = [c for c in top if _benchable(c)]
    space = _space(ctx)
    picks = []
    if pool and space > 0:
        picks = await ctx.choose_cards(pool, min(space, len(pool)), minimum=0, display_cards=top,
                                       prompt="Choose any number of Pokémon to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="974cee01-a2e4-598d-b383-ecc4b7fa6f57",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDelphoxex.Name",
    display_name="Mega Delphox ex",
    searchable_by=["Mega Delphox ex", "Stage 2", "ex", "SV_Mega"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=8,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Trick Portal",
            game_text="Look at the top 9 cards of your deck, and you may put any number of Pokémon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=trick_portal,
        ),
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=ac.condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)
