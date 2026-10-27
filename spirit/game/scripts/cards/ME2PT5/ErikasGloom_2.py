"""Erika's Gloom (ME2PT5 2 -- JP MC 002; English ASC/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="09cbbd07-6881-5097-bcf2-09dc76ab8804",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    display_name="Erika's Gloom",
    searchable_by=["Erika's Gloom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
