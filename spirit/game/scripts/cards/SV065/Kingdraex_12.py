"""Kingdra ex (SV065 12 -- JP SV6a 012; English SFA/12, SFA/80, SVP/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.attributes import PokemonTypes as _PT
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


async def kings_order(ctx):
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c) and _of_type(c, PokemonTypes.WATER)]
    if space <= 0 or not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, space, len(pool)), minimum=0,
                                   prompt="Put up to 3 Water Pokémon from your discard pile onto your Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="7d3d304b-56d2-5bc4-a502-4ec2844a017b",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdraex.Name",
    display_name="Kingdra ex",
    searchable_by=["Kingdra ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=12,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="King's Order",
            game_text="Put up to 3 Water Pokémon from your discard pile onto your Bench.",
            cost={PokemonTypes.WATER: 1},
            effect=kings_order,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 50 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.WATER), 50, base=50),
        ),
    ],
)
