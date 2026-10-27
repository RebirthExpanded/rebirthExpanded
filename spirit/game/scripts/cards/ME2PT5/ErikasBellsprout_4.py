"""Erika's Bellsprout (ME2PT5 4 -- JP MC 006; English ASC/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fc14a9e2-e2d8-5cd6-9765-7a6d96b61cc7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    display_name="Erika's Bellsprout",
    searchable_by=["Erika's Bellsprout", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Vine Slap",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
