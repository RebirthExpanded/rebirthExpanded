"""Flabébé (SV1 91 -- JP SV1V 042; English SVI/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="51d34d8e-78cd-59a0-8625-728bf01e3d79",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    display_name="Flabébé",
    searchable_by=["Flabébé", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=669,
    abilities=[
        Attack(
            title="Pollen Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
