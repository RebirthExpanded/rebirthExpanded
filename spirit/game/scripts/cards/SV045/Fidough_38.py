"""Fidough (SV045 38 -- JP SV1S 032; English PAF/38, SVI/97, SVP/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c68b2c5e-085e-595e-bced-0cfd36df081e",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    display_name="Fidough",
    searchable_by=["Fidough", "Basic"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=926,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
