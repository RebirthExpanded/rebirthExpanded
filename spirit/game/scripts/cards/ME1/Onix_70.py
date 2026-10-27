"""Onix (ME1 70 -- JP M1L 022; English MEG/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fbeb092a-a4d5-5382-97e9-7744bb7f8e9b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
        ),
    ],
)
