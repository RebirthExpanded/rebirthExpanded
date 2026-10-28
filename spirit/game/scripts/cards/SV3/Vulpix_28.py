"""Vulpix (SV3 28 -- JP SV3 014; English OBF/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d759be15-e2f9-5d4e-a8ea-98ae1cd5081e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Confuse Ray",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
