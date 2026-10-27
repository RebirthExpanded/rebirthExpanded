"""Erika's Tangela (ME2PT5 7 -- JP MC 014; English ASC/218, ASC/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.data_utils import def_for


def _is_erikas(card) -> bool:
    return (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith("Erika's ")


def _erikas_pokemon(card) -> bool:
    return is_pokemon_card(card) and _is_erikas(card)


card = PokemonCardDef(
    guid="99edbad4-6d29-5b13-84ea-15cc5a64cd37",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasTangela.Name",
    display_name="Erika's Tangela",
    searchable_by=["Erika's Tangela", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Ability(
            title="Gathering of Blossoms",
            game_text="Once during your turn, you may use this Ability. Search your deck for an Erika's Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=su.requires_deck(),
            effect=su.search_to_hand(_erikas_pokemon, count=1, reveal=True, prompt="Choose an Erika's Pokémon."),
        ),
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
