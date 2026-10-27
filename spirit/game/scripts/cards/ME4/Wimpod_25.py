"""Wimpod (ME4 25 -- JP M4 025; English CRI/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="01682605-6aaa-5631-aae8-fc0a6aa43201",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=767,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
