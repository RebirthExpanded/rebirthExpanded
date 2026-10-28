"""Sableye (SV2 136 -- JP SV1a 055; English PAF/184, PAL/136). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _afflicted(ctx) -> bool:
    d = ctx.opponent_active()
    return d is not None and bool(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="70608282-4993-51fc-8049-11ae2e43fc8c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Night Eyes",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Unseen Claw",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_afflicted, 70),
        ),
    ],
)
