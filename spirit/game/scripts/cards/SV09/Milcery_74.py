"""Milcery (SV09 74 -- JP SVM 059; English JTG/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="709cadab-cc4a-5ee6-8a8f-6f27e7aee84f",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    display_name="Milcery",
    searchable_by=["Milcery", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=868,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
