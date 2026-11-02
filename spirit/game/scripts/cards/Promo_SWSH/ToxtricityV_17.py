"""Toxtricity V (Promo_SWSH 17 -- JP SP 048; English SP/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card


def _lightning_energy_card(card):
    return is_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="9309e6a3-4ce2-5d30-901e-292a4da329cd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityV.Name",
    display_name="Toxtricity V",
    searchable_by=["Toxtricity V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=17,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=849,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.attach_from_discard(_lightning_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Venom Slap",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
