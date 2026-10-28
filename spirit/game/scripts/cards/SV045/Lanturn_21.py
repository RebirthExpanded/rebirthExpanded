"""Lanturn (SV045 21 -- JP SV3a 013; English PAF/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


def _has_water(ctx) -> bool:
    return ac.count_energy("self", _PT.WATER)(ctx) > 0


card = PokemonCardDef(
    guid="1b9e73b9-cdcd-5504-b72e-996b8922215e",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Lightning Ball",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Aqua Spark",
            game_text="If this Pokémon has any Water Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_has_water, 120),
        ),
    ],
)
