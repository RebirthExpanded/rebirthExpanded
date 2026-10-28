"""Falinks (SV2 119 -- JP SV1a 051; English PAL/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _falinks_benched(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Falinks" for p in ctx.my_bench())


card = PokemonCardDef(
    guid="c61db84a-a84f-5032-ad98-52704a5b88ae",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Reckless Charge Together",
            game_text="If Falinks is on your Bench, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_falinks_benched, 90),
        ),
    ],
)
