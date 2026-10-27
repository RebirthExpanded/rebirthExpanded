"""Excadrill (SV08 109 -- JP SV7a 029; English SSP/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _metal_benched(ctx) -> bool:
    return any(_of_type(p, PokemonTypes.METAL) for p in ctx.my_bench())


card = PokemonCardDef(
    guid="23c809bd-f2c0-5052-8ff9-fc9004026e83",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Digging Claw",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.mill_attack(1),
        ),
        Attack(
            title="Drill Smash",
            game_text="If you have any Metal Pokémon on your Bench, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_metal_benched, 80),
        ),
    ],
)
