"""Ferroseed (ME4 62 -- JP M4 060; English CRI/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ff7bbbd7-ed46-576e-83ba-74b7d2497d87",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    display_name="Ferroseed",
    searchable_by=["Ferroseed", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=597,
    abilities=[
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.METAL: 2},
            damage=40,
        ),
    ],
)
