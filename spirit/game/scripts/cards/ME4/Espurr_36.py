"""Espurr (ME4 36 -- JP M4 036; English CRI/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _played_this_turn(ctx, display_name) -> bool:
    for archetype_id, _name, _type in ctx.session.turn_state.trainers_played:
        if getattr(def_for(archetype_id), "display_name", None) == display_name:
            return True
    return False


def _emma(ctx) -> bool:
    return _played_this_turn(ctx, "Emma")


card = PokemonCardDef(
    guid="413acee6-c521-5303-b175-e2de2c4c9f83",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=677,
    abilities=[
        Attack(
            title="Buddy Attack",
            game_text="If you played Emma from your hand during this turn, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(_emma, 60),
        ),
    ],
)
