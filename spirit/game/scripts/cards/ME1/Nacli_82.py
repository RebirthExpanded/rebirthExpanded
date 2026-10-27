"""Nacli (ME1 82 -- JP M1L 034; English MEG/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="29401f3c-2ff2-5910-9abd-766368a25f3f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    display_name="Nacli",
    searchable_by=["Nacli", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=932,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
