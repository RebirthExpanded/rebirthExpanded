"""Beldum (ME4 59 -- JP M4 057; English CRI/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7d1360ba-97c0-5967-9cd7-7c7a40b30784",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=374,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Beam",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
