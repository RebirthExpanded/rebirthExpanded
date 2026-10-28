"""Gyarados (SV2 43 -- JP SV1a 023; English PAL/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _more_left(ctx) -> bool:
    return ac.count_prizes_remaining("mine")(ctx) > ac.count_prizes_remaining("opponent")(ctx)


card = PokemonCardDef(
    guid="89aff78b-7f5e-5426-b2e0-cd6704c2405b",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Revengeful Storm",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_more_left, 100),
        ),
        Attack(
            title="Berserker Tackle",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=ac.recoil_attack(50),
        ),
    ],
)
