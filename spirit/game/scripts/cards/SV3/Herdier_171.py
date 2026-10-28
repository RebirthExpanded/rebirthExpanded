"""Herdier (SV3 171 -- JP SVD 095; English OBF/171). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ef17fd9a-4ebe-5307-babf-9256391eb9d6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    display_name="Herdier",
    searchable_by=["Herdier", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=171,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
