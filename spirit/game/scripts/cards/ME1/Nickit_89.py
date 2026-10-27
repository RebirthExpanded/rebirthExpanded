"""Nickit (ME1 89 -- JP M1L 041; English MEG/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e99fb44e-b0ff-5206-a152-f7bd9670d49a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    display_name="Nickit",
    searchable_by=["Nickit", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=827,
    abilities=[
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
