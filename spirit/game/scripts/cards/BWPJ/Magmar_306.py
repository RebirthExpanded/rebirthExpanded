"""Magmar (BWPJ 306 -- JP WAK 006; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="877fc27e-2a35-5850-9432-9cd5503d3f56",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic"],
    subtypes=["Basic"],
    collector_number=306,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Attack(
            title="Magma Punch",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
