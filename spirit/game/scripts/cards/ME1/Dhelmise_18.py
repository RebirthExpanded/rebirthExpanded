"""Dhelmise (ME1 18 -- JP M1S 009; English MEG/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _my_stadium(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    return stadium is not None and stadium.owning_player_id == ctx.player_id


card = PokemonCardDef(
    guid="33717780-df74-5175-9674-8796be991496",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Earthen Power",
            game_text="If you have a Stadium in play, this attack does 50 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_my_stadium, 50),
        ),
    ],
)
