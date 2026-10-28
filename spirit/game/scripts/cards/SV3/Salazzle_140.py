"""Salazzle (SV3 140 -- JP SV1a 061; English OBF/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ef2ad292-e6a5-5e43-acca-eef2ad85ec43",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name",
    display_name="Salazzle",
    searchable_by=["Salazzle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Attack(
            title="Suffocating Gas",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
