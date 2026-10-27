"""Vullaby (ME2PT5 138 -- JP MC 474; English ASC/138). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8bfd1f6f-0bcd-5a11-bc8f-797ca8345983",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=629,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
