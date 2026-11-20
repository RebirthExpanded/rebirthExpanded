"""Bellsprout (M7 1 -- JP M7 001/078 マダツボミ). Japanese art.

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
    guid="2c7d55e8-875d-5939-a356-f3f973884d02",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name='Bellsprout',
    searchable_by=['Bellsprout', 'Basic', 'Bellsprout'],
    subtypes=['Basic'],
    collector_number=1,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=su.search_to_hand(is_pokemon_card, count=1, reveal=True, prompt='Choose a Pokémon'),
        ),
    ],
)
