"""Meloetta (M7 32 -- JP M7 032/078 メロエッタ). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import m7
from spirit.game.card_effects.pokemon import AttackTwicePassive
from spirit.game.session.effects import is_pokemon_card, is_supporter_card


card = PokemonCardDef(
    guid="cb73568d-9358-5426-9d60-b9cee8ae83b2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name='Meloetta',
    searchable_by=['Meloetta', 'Basic', 'Meloetta'],
    subtypes=['Basic'],
    collector_number=32,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=648,
    abilities=[
        Attack(
            title='Welcoming Song',
            game_text='Search your deck for up to 3 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=3, prompt='Choose up to 3 Basic Pokémon'),
        ),
        Attack(
            title='Bewilder',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=m7.bewilder,
        ),
    ],
)
