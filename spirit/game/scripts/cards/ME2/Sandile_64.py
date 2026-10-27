"""Sandile (ME2 64 -- JP M2 053; English PFL/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="12f3ff2b-1dec-5907-b348-0974a9685cab",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=551,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
