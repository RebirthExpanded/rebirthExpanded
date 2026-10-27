"""Arcanine (ME6 11 -- JP M6 011; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _four_or_fewer(ctx) -> bool:
    return ac.count_prizes_remaining("opponent")(ctx) <= 4


card = PokemonCardDef(
    guid="f609c91e-26a2-5244-aa8e-7e518c2c84e9",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Spirited Fang",
            game_text="If your opponent has 4 or fewer Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_four_or_fewer, 90),
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=ac.recoil_attack(50),
        ),
    ],
)
