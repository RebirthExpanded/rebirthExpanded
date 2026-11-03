"""Cobalion (BWPJ 340 -- JP WAK 040; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f16c014a-0abe-5b0a-9df2-d6693c487b42",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic"],
    subtypes=["Basic"],
    collector_number=340,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Attack(
            title="Metal Claw",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
