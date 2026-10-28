"""Magmar (SV035 126 -- JP SV2a 126; English MEW/126). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _electabuzz(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Electabuzz" for p in ctx.my_bench())


card = PokemonCardDef(
    guid="e1b3796d-06ba-51d6-a852-aa79bdf647b0",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Flare Combo",
            game_text="If Electabuzz is on your Bench, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_electabuzz, 80),
        ),
    ],
)
