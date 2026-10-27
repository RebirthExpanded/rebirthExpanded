"""Dhelmise (SV05 19 -- JP SV5M 011; English TEF/19). Japanese art.
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
    guid="44c77241-d2f3-5ec1-90fa-da008e3eb5ee",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Steel Anchor",
            game_text="If you have any Metal Pokémon on your Bench, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_metal_benched, 80),
        ),
    ],
)
