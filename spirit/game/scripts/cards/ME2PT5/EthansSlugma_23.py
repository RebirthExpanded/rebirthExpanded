"""Ethan's Slugma (ME2PT5 23 -- JP SV9a 018; English ASC/23, DRI/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f623739c-03ac-5e84-a608-b410d7c71976",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    display_name="Ethan's Slugma",
    searchable_by=["Ethan's Slugma", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
