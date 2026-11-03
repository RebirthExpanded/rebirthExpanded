"""Deerling (BWPJ 304 -- JP WAK 004; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b15b342c-67ba-579e-a0f2-42e264eea69e",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    display_name="Deerling",
    searchable_by=["Deerling", "Basic"],
    subtypes=["Basic"],
    collector_number=304,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=585,
    abilities=[
        Attack(
            title="Back Kick",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
