"""Venusaur V (Promo_SWSH 100 -- JP SEF 001; English SP/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c2d905a0-b843-5a5f-a490-b458497cf8ad",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name",
    display_name="Venusaur V",
    searchable_by=["Venusaur V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=100,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Leaf Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=ac.recoil_attack(30),
        ),
    ],
)
