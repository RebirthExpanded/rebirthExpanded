"""Houndstone ex (SVP 162 -- JP SVI 028; English SVP/162). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5e174545-1b3d-59ef-88c4-c0044cf5ec78",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstoneex.Name",
    display_name="Houndstone ex",
    searchable_by=["Houndstone ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=162,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Horrifying Fang",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)
