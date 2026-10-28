"""Cufant (SV2 149 -- JP SV2P 053; English PAL/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="99c47476-f1e9-59a1-851e-f1a268d35eaf",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    display_name="Cufant",
    searchable_by=["Cufant", "Basic"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=878,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
