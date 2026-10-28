"""Parasect (SV035 47 -- JP SV2a 047; English MEW/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def spread_filaments(ctx):
    heads = sum(1 for r in await ctx.flip_coins(2, "Spread Filaments") if r)
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    take = min(heads, space)
    if take > 0:
        picks = await ctx.search_deck(lambda c: is_basic_pokemon(c) and _of_type(c, PokemonTypes.GRASS),
                                      count=take, minimum=0, prompt="Choose Grass Pokémon to put onto your Bench.")
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="8cd35d4a-e011-5d53-8def-5579b5677340",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Spread Filaments",
            game_text="Flip 2 coins. Search your deck for a number of Grass Pokémon up to the number of heads and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=spread_filaments,
        ),
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
