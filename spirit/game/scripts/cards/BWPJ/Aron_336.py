"""Aron (BWPJ 336 -- JP WAK 036; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="01fa5a8b-41df-59ea-a9ba-a7d35a4897ed",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic"],
    subtypes=["Basic"],
    collector_number=336,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=304,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
