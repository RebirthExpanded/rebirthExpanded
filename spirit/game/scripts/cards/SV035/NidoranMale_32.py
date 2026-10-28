"""Nidoran ♂ (SV035 32 -- JP SV2a 032; English MEW/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d9015821-2f03-5bc3-932f-a90b5cd65832",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranMale.Name",
    display_name="Nidoran ♂",
    searchable_by=["Nidoran ♂", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=32,
    abilities=[
        Attack(
            title="Horn Attack",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
