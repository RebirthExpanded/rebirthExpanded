"""Nincada (ME1 16 -- JP M1S 007; English MEG/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e5ba9f2a-7fab-5a6f-a4c3-2b3672e50d2d",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    display_name="Nincada",
    searchable_by=["Nincada", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=290,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
