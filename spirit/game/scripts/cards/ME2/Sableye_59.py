"""Sableye (ME2 59 -- JP MBG 006; English PFL/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_stage2_pokemon


def _stage2_dark_benched(ctx) -> bool:
    return any(is_stage2_pokemon(p) and _of_type(p, PokemonTypes.DARKNESS) for p in ctx.my_bench())


card = PokemonCardDef(
    guid="1e81a7d7-eedf-5d00-a9b2-eada92b3c750",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Cocky Claw",
            game_text="If you have any Stage 2 Darkness Pokémon on your Bench, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_stage2_dark_benched, 70),
        ),
    ],
)
