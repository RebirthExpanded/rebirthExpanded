"""Hippowdon (SV085 53 -- JP SVM 067; English PRE/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="29dbe9e9-eeb7-5c9a-bba5-4551ed300629",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Sand Spray",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
        Attack(
            title="Land Crush",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
