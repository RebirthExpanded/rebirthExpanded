"""Varoom (SV06 124 -- JP SV6 077; English TWM/124). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


card = PokemonCardDef(
    guid="fa84eeb6-445f-53c5-9cbf-d54ad17a2742",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name="Varoom",
    searchable_by=["Varoom", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=965,
    abilities=[
        Attack(
            title="Metal Coating",
            game_text="Attach a Basic Metal Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.attach_from_discard(_basic_metal, count=1, target="self", minimum=0, prompt="Attach a Basic Metal Energy card from your discard pile to this Pokémon."),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
