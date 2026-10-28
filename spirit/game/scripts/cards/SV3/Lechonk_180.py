"""Lechonk (SV3 180 -- JP SV3 096; English OBF/180, OBF/209). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="1c3f4487-d814-5ad2-8eb8-a7c040eec46d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    display_name="Lechonk",
    searchable_by=["Lechonk", "Basic"],
    subtypes=["Basic"],
    collector_number=180,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=915,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
