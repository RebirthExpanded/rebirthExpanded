"""Houndstone (SV045 43 -- JP SV1V 048; English PAF/168, PAF/43, SVI/106). Japanese art.
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
    guid="acec88a0-6ed7-5d33-86f7-ddc9942ffa67",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Last Respects",
            game_text="This attack does 10 more damage for each Psychic Pokémon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=80,
            damage_operator="+",
            effect=ac.damage_per(_psychic_discard, 10, base=80),
        ),
    ],
)
