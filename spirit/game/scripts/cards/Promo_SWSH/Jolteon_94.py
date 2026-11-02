"""Jolteon (Promo_SWSH 94 -- JP SP 114; English SP/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card


def _lightning_energy_card(card):
    return is_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="cee159b1-cf0b-5893-ae1b-2384faa7dbad",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=su.attach_from_discard(_lightning_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.recoil_attack(30),
        ),
    ],
)
