"""Zacian ex (SVP 198 -- JP SVM 089; English SVP/198). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


card = PokemonCardDef(
    guid="fce5f35f-9454-5b9a-ab68-ca3491a06e8f",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacianex.Name",
    display_name="Zacian ex",
    searchable_by=["Zacian ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=198,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title="Steel Armament",
            game_text="Search your deck for a Basic [M] Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.search_attach_energy(_basic_metal, count=1, to_self=True, prompt="Choose a Basic Metal Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pokémon can't use Slashing Strike.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)
