"""Ariados (ME3 2 -- JP M3 002; English POR/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="604ddcd7-42ab-5473-ad36-00960dd87977",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
    ],
)
