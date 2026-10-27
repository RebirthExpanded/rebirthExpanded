"""Ninetales (SV06 27 -- JP SV5a 011; English TWM/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="80a887ef-fb24-5a0f-9e26-d14b11cb1e78",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            effect=ac.condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)
