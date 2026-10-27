"""Gastly (ME2 54 -- JP MBG 001; English ASC/123, PFL/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6d39c884-38a2-598f-9cd8-744eff6609ae",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Petty Grudge",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
