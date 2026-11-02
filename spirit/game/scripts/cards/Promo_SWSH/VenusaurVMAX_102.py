"""Venusaur VMAX (Promo_SWSH 102 -- JP SEF 002; English SP/102). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes

_grass_in_play = ac.count_energy("mine", energy_type=PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="780e6a16-11dd-5f66-82cd-1b151d2619fa",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurVMAX.Name",
    display_name="Venusaur VMAX",
    searchable_by=["Venusaur VMAX", "VMAX"],
    subtypes=["VMAX"],
    collector_number=102,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name",
    family_id=3,
    abilities=[
        Attack(
            title="Forest Storm",
            game_text="This attack does 30 damage for each Grass Energy attached to all of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(_grass_in_play, 30),
        ),
        Attack(
            title="G-Max Bloom",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=210,
            effect=su.heal_attack(30),
        ),
    ],
)
