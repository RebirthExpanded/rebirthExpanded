"""Dwebble (SV4 6 -- JP SV4K 004; English PAR/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="5c957e5d-ed9b-51d4-8fc2-47b7c7215b9f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    display_name="Dwebble",
    searchable_by=["Dwebble", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=557,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
