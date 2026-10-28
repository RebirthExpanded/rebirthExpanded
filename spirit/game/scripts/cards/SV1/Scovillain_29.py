"""Scovillain (SV1 29 -- JP SV1V 014; English SVI/202, SVI/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


def _has_fire(ctx) -> bool:
    return ac.count_energy("self", _PT.FIRE)(ctx) > 0


card = PokemonCardDef(
    guid="144e8397-f82c-58bd-a1fc-686ff8a6c271",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillain.Name",
    display_name="Scovillain",
    searchable_by=["Scovillain", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Attack(
            title="Hot Bite",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Super Spicy Breath",
            game_text="If this Pokémon has any Fire Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_has_fire, 90),
        ),
    ],
)
