"""Fletchling (ME3 66 -- JP M3 065; English POR/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.attributes import AttrID


def _fighting_resistance(card) -> bool:
    res = card.get_attribute(AttrID.RESISTANCE_TYPES)
    res = res if isinstance(res, (list, tuple)) else ([res] if res is not None else [])
    return is_pokemon_card(card) and PokemonTypes.FIGHTING.value in res


card = PokemonCardDef(
    guid="88a827e6-0faa-5000-bbfd-a88d3927054d",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    display_name="Fletchling",
    searchable_by=["Fletchling", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=661,
    abilities=[
        Attack(
            title="Chirp",
            game_text="Search your deck for up to 2 Pokémon with Fighting Resistance, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(_fighting_resistance, count=2, reveal=True, prompt="Choose up to 2 Pokémon with Fighting Resistance."),
        ),
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
