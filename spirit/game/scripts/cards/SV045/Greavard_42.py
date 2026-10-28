"""Greavard (SV045 42 -- JP SV1V 046; English PAF/42, SVI/104, SVI/214, SVP/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_pokemon_card


def _psychic_discard(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c) and _of_type(c, PokemonTypes.PSYCHIC))


card = PokemonCardDef(
    guid="c1a4483d-1e5b-5b29-bf99-31b6343c9d5f",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    display_name="Greavard",
    searchable_by=["Greavard", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title="Graveyard Gamboling",
            game_text="This attack does 10 damage for each Psychic Pokémon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=ac.damage_per(_psychic_discard, 10),
        ),
    ],
)
