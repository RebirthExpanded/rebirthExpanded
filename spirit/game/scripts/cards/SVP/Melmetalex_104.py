"""Melmetal ex (SVP 104 -- JP SVD 085; English OBF/153, SVP/104). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="48391144-2bc7-5230-8767-45f168da2617",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetalex.Name",
    display_name="Melmetal ex",
    searchable_by=["Melmetal ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=104,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Metal-bolize",
            game_text="Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=su.search_attach_energy(_basic_metal, count=2, to_self=True, prompt="Choose up to 2 Basic Metal Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Full Metal Knuckle",
            game_text="This attack does 30 more damage for each Metal Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.METAL), 30, base=90),
        ),
    ],
)
