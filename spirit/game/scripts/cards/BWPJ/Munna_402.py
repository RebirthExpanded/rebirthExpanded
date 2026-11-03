"""Munna (BWPJ 402 -- JP CS1 002; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7a460664-ebf2-5c75-ac6d-e58e6db07cb5",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic"],
    subtypes=["Basic"],
    collector_number=402,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=517,
    abilities=[
        Attack(
            title="Yawn",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
