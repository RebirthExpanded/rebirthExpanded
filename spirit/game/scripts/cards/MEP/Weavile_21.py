"""Weavile (MEP 21 -- JP M2 049; English MEP/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _low_hp(ctx) -> bool:
    return (ctx.attacker.get_attribute(AttrID.HP, 0) or 0) <= 50


card = PokemonCardDef(
    guid="3d8c2a2f-7936-5b42-9341-f8b764b92134",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Retaliatory Claw",
            game_text="If this Pokémon's remaining HP is 50 or less, this attack does 170 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_low_hp, 170),
        ),
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
    ],
)
