"""Oddish (ME2 1 -- JP M2 001; English PFL/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="cd4e545c-4074-5508-a697-7c7bfcb40bdb",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Seed Bomb",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
