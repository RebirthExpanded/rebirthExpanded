"""Aromatisse (ME3 36 -- JP M3 035; English POR/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)


card = PokemonCardDef(
    guid="957dd1bc-d85f-5232-aeb2-2b828a401a4f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name",
    display_name="Aromatisse",
    searchable_by=["Aromatisse", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    family_id=682,
    abilities=[
        Ability(
            title="Scent Collection",
            game_text="Once during your turn, you may use this Ability. Search your deck for up to 2 Basic Psychic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=su.requires_deck(),
            effect=su.search_to_hand(_basic_psychic, count=2, reveal=True, prompt="Choose up to 2 Basic Psychic Energy cards."),
        ),
        Attack(
            title="Draining Kiss",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.heal_attack(30),
        ),
    ],
)
