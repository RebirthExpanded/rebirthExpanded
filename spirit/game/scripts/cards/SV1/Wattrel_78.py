"""Wattrel (SV1 78 -- JP SV1S 024; English SVI/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="bc7f8df3-9536-5e87-99aa-407eb7ec161d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    display_name="Wattrel",
    searchable_by=["Wattrel", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=940,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
