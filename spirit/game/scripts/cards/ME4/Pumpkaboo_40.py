"""Pumpkaboo (ME4 40 -- JP M4 040; English CRI/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0ac5ec61-7578-525a-8941-ccaf7d1571b3",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=710,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
