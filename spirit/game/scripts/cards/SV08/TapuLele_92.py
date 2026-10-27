"""Tapu Lele (SV08 92 -- JP SV7a 021; English SSP/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="917a2321-474a-53bb-a68a-00aec30d21a4",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name",
    display_name="Tapu Lele",
    searchable_by=["Tapu Lele", "Basic"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=786,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Mental Crush",
            game_text="If your opponent's Active Pokémon is Confused, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.CONFUSED), 90),
        ),
    ],
)
