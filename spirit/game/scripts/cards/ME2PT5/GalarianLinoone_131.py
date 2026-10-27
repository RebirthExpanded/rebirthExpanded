"""Galarian Linoone (ME2PT5 131 -- JP M2a 106; English ASC/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="bd2e34e5-0109-5de1-9e2a-a67143a13eb0",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    display_name="Galarian Linoone",
    searchable_by=["Galarian Linoone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
