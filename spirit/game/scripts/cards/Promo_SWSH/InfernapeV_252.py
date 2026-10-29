"""Infernape V (Promo_SWSH 252 -- JP SP 257; English SP/252). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0322ab24-c63e-5dd8-bdfb-41609bc62587",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeV.Name",
    display_name="Infernape V",
    searchable_by=["Infernape V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=252,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Meteor Punch",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=30),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.self_energy_discard_attack(2),
        ),
    ],
)
