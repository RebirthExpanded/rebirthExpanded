"""Cyclizar (SV4 157 -- JP SV3a 052; English PAR/157, PAR/215). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import TrainerType


def _supporter_played(ctx) -> bool:
    return any(ttype == TrainerType.SUPPORTER.value for _a, _n, ttype in ctx.session.turn_state.trainers_played)


card = PokemonCardDef(
    guid="f533f67a-40fe-5bdd-b6bc-3cdf1ddb7fe4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name",
    display_name="Cyclizar",
    searchable_by=["Cyclizar", "Basic"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Driving Buddy",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_supporter_played, 70),
        ),
    ],
)
