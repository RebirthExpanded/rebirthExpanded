"""Tangela (BWPJ 301 -- JP WAK 001; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="571669ea-177c-5355-a2cb-7d706c76e9f9",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic"],
    subtypes=["Basic"],
    collector_number=301,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=114,
    abilities=[
        Attack(
            title="Vine Whip",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
