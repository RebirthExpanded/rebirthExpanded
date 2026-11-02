"""Shadow Rider Calyrex V (Promo_SWSH 131 -- JP SP3 002; English SP/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card


def _psychic_energy_card(card):
    return is_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)


card = PokemonCardDef(
    guid="a433aab0-797c-5ed7-bfef-9c80478cba5f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name",
    display_name="Shadow Rider Calyrex V",
    searchable_by=["Shadow Rider Calyrex V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=131,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=898,
    abilities=[
        Attack(
            title="Cloak in Shadows",
            game_text="Attach a Psychic Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.attach_from_discard(_psychic_energy_card, count=1, target="self", minimum=0),
        ),
        Attack(
            title="Hollow Binding",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
