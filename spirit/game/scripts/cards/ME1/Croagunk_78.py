"""Croagunk (ME1 78 -- JP M1L 030; English MEG/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="5c6e38dc-44f1-5513-9d76-76d0adba460b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Smack",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
