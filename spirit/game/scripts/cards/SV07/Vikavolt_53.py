"""Vikavolt (SV07 53 -- JP SV7 035; English ASC/230, ASC/66, SCR/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _lightning(p) -> bool:
    return _of_type(p, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="62879f98-cd5f-57a2-af54-15ff06936bb9",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=53,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Volt Switch",
            game_text="Switch this Pokémon with 1 of your Benched Lightning Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=90,
            effect=su.switch_self_attack(bench_predicate=_lightning),
        ),
        Attack(
            title="Sparking Strike",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
        ),
    ],
)
