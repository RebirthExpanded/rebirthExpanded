"""Pikachu VMAX (Promo_SWSH 286 -- JP SP 265; English SP/286). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="fb9f8a08-ed92-5289-a80f-e99ba1f0ff0f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVMAX.Name",
    display_name="Pikachu VMAX",
    searchable_by=["Pikachu VMAX", "VMAX"],
    subtypes=["VMAX"],
    collector_number=286,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Tail Charge",
            game_text="Attach up to 3 Lightning Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=su.attach_from_discard(_basic_lightning, count=3, target="choice", minimum=0),
        ),
        Attack(
            title="G-Max Thunder",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=250,
        ),
    ],
)
