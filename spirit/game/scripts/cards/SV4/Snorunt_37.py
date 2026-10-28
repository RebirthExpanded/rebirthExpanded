"""Snorunt (SV4 37 -- JP SV3a 005; English PAR/188, PAR/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _fighting(p) -> bool:
    return _of_type(p, PokemonTypes.FIGHTING)


card = PokemonCardDef(
    guid="78245e1c-f91f-5e31-880e-3bc54e73fdb0",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    display_name="Snorunt",
    searchable_by=["Snorunt", "Basic"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pokémon is a Fighting Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(ac.active_is(_fighting), 30),
        ),
    ],
)
