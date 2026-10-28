"""Electabuzz (SV035 125 -- JP SV2a 125; English MEW/125). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _magmar(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Magmar" for p in ctx.my_bench())


card = PokemonCardDef(
    guid="21f64746-f369-5903-9be3-43a5156c519f",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Attack(
            title="Electro Combo",
            game_text="If Magmar is on your Bench, this attack does 40 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(_magmar, 40),
        ),
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
