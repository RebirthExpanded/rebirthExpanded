"""Sneasel (MEP 20 -- JP M2 048; English MEP/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="36d9cec5-76c1-5e32-9b7d-cfa806f96660",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=215,
    abilities=[
        Attack(
            title="Dig Claws",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)
