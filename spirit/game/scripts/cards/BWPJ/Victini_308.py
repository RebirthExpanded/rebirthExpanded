"""Victini (BWPJ 308 -- JP WAK 008; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="72b52774-803a-5593-8097-a7e857a62612",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic"],
    subtypes=["Basic"],
    collector_number=308,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="V Flame",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
