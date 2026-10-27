"""Amoonguss (ZSV10PT5 11 -- JP SV11B 011; English BLK/11, BLK/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _any_condition(ctx) -> bool:
    d = ctx.opponent_active()
    return d is not None and bool(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="f1cbf781-42ff-5f0c-a4d7-34e707113a45",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Dangerous Reaction",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_any_condition, 120),
        ),
        Attack(
            title="Seed Bomb",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
