"""Tangela (SV035 114 -- JP SV2a 114; English MEW/114, MEW/178). Japanese art.
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


def _erika_played(ctx) -> bool:
    return _played_this_turn(ctx, "Erika's Invitation")


card = PokemonCardDef(
    guid="e6679d74-9b57-5f1e-9633-a12e9037b988",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Attack(
            title="Tactful Tangling",
            game_text="If you played Erika's Invitation from your hand during this turn, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(_erika_played, 60),
        ),
    ],
)
