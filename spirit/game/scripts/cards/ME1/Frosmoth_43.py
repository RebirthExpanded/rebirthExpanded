"""Frosmoth (ME1 43 -- JP M1S 025; English MEG/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="67d261b6-901d-5cca-8a69-02db39657562",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Attack(
            title="Chilling Wings",
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=ac.damage_all_opponents(20, also=ac.condition_attack(SpecialConditions.ASLEEP, damage=0)),
        ),
    ],
)
