"""Shaymin (BWPJ 233 -- JP BWP 233; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)

from spirit.game.card_effects.pokemon import is_energy_card


def _grass_energy(card):
    return is_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


def _benched(pokemon):
    return pokemon is not None and pokemon._containing_area_name() == "bench"


card = PokemonCardDef(
    guid="be40a92d-4647-5b76-b1c0-e3893281e5ab",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic"],
    subtypes=["Basic"],
    collector_number=233,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach a [G] Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=su.attach_from_discard(_grass_energy, count=1, target=_benched, prompt="Choose a [G] Energy card to attach to 1 of your Benched Pokémon."),
        ),
        Attack(
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=20),
        ),
    ],
)
