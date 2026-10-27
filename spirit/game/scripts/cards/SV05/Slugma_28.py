"""Slugma (SV05 28 -- JP SV5M 017; English TEF/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="79bbd15a-4424-5f33-8a5a-cec4eb79ee13",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If your opponent's Active Pokémon is Burned, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.BURNED), 40),
        ),
    ],
)
