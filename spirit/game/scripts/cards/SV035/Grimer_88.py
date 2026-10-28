"""Grimer (SV035 88 -- JP SV2a 088; English MEW/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="0f630861-bd9a-5f73-b2d3-dd0156f672a3",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=88,
    abilities=[
        Attack(
            title="Gummy Press",
            game_text="During your opponent's next turn, the Defending Pokémon's Retreat Cost is Colorless more.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=pc.raise_defender_retreat_cost_next_turn(1),
        ),
    ],
)
