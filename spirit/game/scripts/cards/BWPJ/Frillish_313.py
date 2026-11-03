"""Frillish (BWPJ 313 -- JP WAK 013; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f89877f5-f3d1-5744-be64-6f962a756221",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    display_name="Frillish",
    searchable_by=["Frillish", "Basic"],
    subtypes=["Basic"],
    collector_number=313,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=592,
    abilities=[
        Attack(
            title="Splash",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
