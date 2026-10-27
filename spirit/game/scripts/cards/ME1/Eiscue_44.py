"""Eiscue (ME1 44 -- JP M1S 026; English MEG/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e22bc920-cf8e-529a-abae-1d5f0420a9e2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Freezing Headbutt",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
