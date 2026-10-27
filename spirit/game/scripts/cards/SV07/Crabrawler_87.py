"""Crabrawler (SV07 87 -- JP SV7 059; English SCR/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="03996b8f-7734-5cd7-a77f-775e6029535f",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    display_name="Crabrawler",
    searchable_by=["Crabrawler", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=739,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Crabhammer",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
