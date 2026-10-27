"""Flutter Mane (SV08 96 -- JP SV8 059; English SSP/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


async def perplexing_transfer(ctx):
    pool = [p for p in ctx.my_bench() if _has_sub(p, "Ancient") and _counters(ctx.board, p) > 0]
    d = ctx.opponent_active()
    if not pool or d is None:
        return
    source = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Ancient Pokémon")
    if source is not None:
        await ctx.move_damage_counters(source, d)


card = PokemonCardDef(
    guid="c203994d-5d26-5c15-bd91-00799103dc08",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlutterMane.Name",
    display_name="Flutter Mane",
    searchable_by=["Flutter Mane", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=96,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=987,
    abilities=[
        Attack(
            title="Perplexing Transfer",
            game_text="Move all damage counters from 1 of your Benched Ancient Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=perplexing_transfer,
        ),
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            effect=pc.debuff_defender_attacks(30),
        ),
    ],
)
