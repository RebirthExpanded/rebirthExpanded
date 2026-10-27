"""Gothita (RSV10PT5 41 -- JP SV11W 038; English WHT/124, WHT/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="92a2535e-d29d-5ad8-973e-f98da7fd0983",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=574,
    abilities=[
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
