"""Honedge (SV4 130 -- JP SV3a 045; English PAR/130). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="443a5584-b6df-50ae-aec6-250be5c8d40f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    display_name="Honedge",
    searchable_by=["Honedge", "Basic"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=679,
    abilities=[
        Attack(
            title="Cut Up",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)
