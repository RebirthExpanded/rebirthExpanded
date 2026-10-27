"""Snom (SV05 45 -- JP SV5K 019; English TEF/168, TEF/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bae8c5ca-ae43-5f0a-9619-8ba54e85744a",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    display_name="Snom",
    searchable_by=["Snom", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=872,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
