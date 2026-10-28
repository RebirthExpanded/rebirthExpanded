"""Starly (SV1 148 -- JP SV1S 063; English SVI/148, SVI/221). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="df16f622-14d7-56ac-9818-de57209b6f94",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    display_name="Starly",
    searchable_by=["Starly", "Basic"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=396,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
