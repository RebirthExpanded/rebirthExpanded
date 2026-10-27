"""Gigalith (RSV10PT5 48 -- JP SV11W 045; English WHT/129, WHT/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _bench_fighting_counters(ctx) -> int:
    return sum(_counters(ctx.board, p) for p in ctx.my_bench() if _of_type(p, PokemonTypes.FIGHTING))


card = PokemonCardDef(
    guid="82d9b89f-a179-56f1-a638-405af16e67ae",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=48,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Vengeful Cannon",
            game_text="This attack does 20 damage for each damage counter on all of your Benched Fighting Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_bench_fighting_counters, 20),
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIGHTING: 3},
            damage=160,
        ),
    ],
)
