"""Galarian Zigzagoon (ME2PT5 130 -- JP M2a 105; English ASC/130). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b498209f-d518-5fd2-a937-74cec7b1f22e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    display_name="Galarian Zigzagoon",
    searchable_by=["Galarian Zigzagoon", "Basic"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=263,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
