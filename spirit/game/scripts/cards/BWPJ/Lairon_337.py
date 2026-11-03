"""Lairon (BWPJ 337 -- JP WAK 037; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="98657c43-94b7-5939-bdf3-12d02b7a8812",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=337,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
