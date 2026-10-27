"""Chespin (ME4 5 -- JP M4 005; English CRI/5, CRI/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e2bcc553-df19-5cdb-858e-9dd31304fa44",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Spike Sting",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)
