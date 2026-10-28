"""Nidoran ♀ (SV035 29 -- JP SV2a 029; English MEW/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bbb96adc-10ac-5656-ba0b-45a002b808b9",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran ♀", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=29,
    abilities=[
        Attack(
            title="Poison Horn",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
