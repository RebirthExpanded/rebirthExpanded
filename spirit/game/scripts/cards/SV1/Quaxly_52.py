"""Quaxly (SV1 52 -- JP SVAW 002; English SVI/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8383a8c5-cffb-5471-bac4-9c9e06229d22",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    display_name="Quaxly",
    searchable_by=["Quaxly", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=912,
    abilities=[
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Kick",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
