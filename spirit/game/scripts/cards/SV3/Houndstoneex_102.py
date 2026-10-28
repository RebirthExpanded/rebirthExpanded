"""Houndstone ex (SV3 102 -- JP SVP1 007; English OBF/102). Japanese art.
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
    guid="98dd6a62-e926-53b9-8a54-ecd5da082835",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstoneex.Name",
    display_name="Houndstone ex",
    searchable_by=["Houndstone ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=102,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
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
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Last Respects",
            game_text="This attack does 10 more damage for each Psychic Pokémon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            damage_operator="+",
            effect=ac.damage_per(_psychic_discard, 10, base=160),
        ),
    ],
)
