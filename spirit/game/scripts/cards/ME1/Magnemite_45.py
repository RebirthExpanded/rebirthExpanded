"""Magnemite (ME1 45 -- JP M1S 027; English MEG/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6acbda58-3959-5976-8e9a-ba91f35195a7",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Beam",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
