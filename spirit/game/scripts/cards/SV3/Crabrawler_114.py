"""Crabrawler (SV3 114 -- JP SV2D 042; English OBF/114). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9f5282ad-f188-539b-9907-befa6471b638",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    display_name="Crabrawler",
    searchable_by=["Crabrawler", "Basic"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=739,
    abilities=[
        Attack(
            title="Knuckle Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Magnum Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
