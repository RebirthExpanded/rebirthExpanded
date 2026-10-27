"""Gliscor (ME2 50 -- JP M2 044; English PFL/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="48eb5758-d6fa-523c-a33c-a4e3f420b71a",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
    ],
)
