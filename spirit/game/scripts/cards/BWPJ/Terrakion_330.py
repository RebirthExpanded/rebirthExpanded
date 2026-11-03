"""Terrakion (BWPJ 330 -- JP WAK 030; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f60f5dfc-d11e-5f2d-be10-7074680c96be",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terrakion.Name",
    display_name="Terrakion",
    searchable_by=["Terrakion", "Basic"],
    subtypes=["Basic"],
    collector_number=330,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Rock Throw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
