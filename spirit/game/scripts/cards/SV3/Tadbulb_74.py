"""Tadbulb (SV3 74 -- JP SV3 039; English OBF/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="8f753959-d9a7-5a4e-bb11-13fcdb22805d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    display_name="Tadbulb",
    searchable_by=["Tadbulb", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Basic Lightning Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=su.attach_from_discard(_basic_lightning, count=1, target="self", minimum=0, prompt="Attach a Basic Lightning Energy card from your discard pile to this Pokémon."),
        ),
        Attack(
            title="Lightning Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
