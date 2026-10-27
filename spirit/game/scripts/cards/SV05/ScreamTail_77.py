"""Scream Tail (SV05 77 -- JP SVHK 007; English TEF/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


async def supportive_singing(ctx):
    pool = [p for p in ctx.my_bench() if _has_sub(p, "Ancient") and _counters(ctx.board, p) > 0]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Ancient Pokémon to heal 100 damage from")
    if target is not None:
        await ctx.heal(100, target)


card = PokemonCardDef(
    guid="8c7af31a-623c-5111-b085-56f5a774aaf9",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTail.Name",
    display_name="Scream Tail",
    searchable_by=["Scream Tail", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=77,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=985,
    abilities=[
        Attack(
            title="Supportive Singing",
            game_text="Heal 100 damage from 1 of your Benched Ancient Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=supportive_singing,
        ),
        Attack(
            title="Hyper Voice",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
