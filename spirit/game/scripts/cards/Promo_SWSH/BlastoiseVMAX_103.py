"""Blastoise VMAX (Promo_SWSH 103 -- JP SEK 002; English SP/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.passives_common import is_in_active_spot


def _water_energy(card):
    return is_energy_of_type(card, PokemonTypes.WATER)


def _benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)


card = PokemonCardDef(
    guid="a67b5178-22b9-5954-aa83-5d6dd7c310c9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseVMAX.Name",
    display_name="Blastoise VMAX",
    searchable_by=["Blastoise VMAX", "VMAX"],
    subtypes=["VMAX"],
    collector_number=103,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseV.Name",
    family_id=9,
    abilities=[
        Attack(
            title="Grand Falls",
            game_text="Search your deck for up to 3 Water Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=su.search_attach_energy(_water_energy, count=3, target_pred=_benched),
        ),
        Attack(
            title="G-Max Bombard",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 4},
            damage=220,
            effect=ac.snipe_attack(30, pool="bench", count=2, also_base=True),
        ),
    ],
)
