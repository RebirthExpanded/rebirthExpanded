"""Copperajah (SV09 110 -- JP SVM 087; English JTG/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9521de3a-0537-5410-9936-3dae8a3f0851",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
        Attack(
            title="Mega Impact",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
