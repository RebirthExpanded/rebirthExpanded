"""Abra (SV035 63 -- JP SV2a 063; English MEW/63, PAF/148). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0aed5116-591a-5fed-a8ed-f38b3177883c",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=63,
    abilities=[
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
