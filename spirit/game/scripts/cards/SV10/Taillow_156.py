"""Taillow (SV10 156 -- JP SV10 084; English DRI/156). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fc4f6768-e0b6-5d7b-b711-a434fdca509b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    display_name="Taillow",
    searchable_by=["Taillow", "Basic"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=276,
    abilities=[
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
