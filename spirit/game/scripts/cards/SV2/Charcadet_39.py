"""Charcadet (SV2 39 -- JP SV2D 015; English PAL/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6040d5e1-f35d-557c-913f-18224093e690",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Magnum Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
