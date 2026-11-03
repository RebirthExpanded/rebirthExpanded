"""Throh (BWPJ 328 -- JP WAK 028; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f39ef92d-e14a-5270-8fc8-604b7779d2dc",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic"],
    subtypes=["Basic"],
    collector_number=328,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Palm Strike",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
