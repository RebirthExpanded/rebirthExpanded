"""Lechonk (SV3 181 -- JP SV3 097; English OBF/181). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="889d2ae9-1436-5727-b419-fdece64da197",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    display_name="Lechonk",
    searchable_by=["Lechonk", "Basic"],
    subtypes=["Basic"],
    collector_number=181,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=915,
    abilities=[
        Attack(
            title="Disarming Voice",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
