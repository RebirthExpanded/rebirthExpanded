"""Dedenne ex (SV2 93 -- JP SV1a 038; English PAL/239, PAL/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def tail_swap(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    d = ctx.opponent_active()
    if not pool or d is None:
        return
    source = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon")
    if source is not None:
        await ctx.move_damage_counters(source, d)


card = PokemonCardDef(
    guid="9869d274-3e8e-5472-a412-c8b8a5b3cdd1",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenneex.Name",
    display_name="Dedenne ex",
    searchable_by=["Dedenne ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=93,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Tail Swap",
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=tail_swap,
        ),
        Attack(
            title="Wondrous Shot",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=170,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
