"""Buizel (M7 19 -- JP M7 019/078 ブイゼル). Japanese art.

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
    guid="7c6622c4-8584-5c05-b3ad-a6c70e815228",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    display_name='Buizel',
    searchable_by=['Buizel', 'Basic', 'Buizel'],
    subtypes=['Basic'],
    collector_number=19,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=418,
    abilities=[
        Attack(
            title='Lead',
            game_text='Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_supporter_card, count=1, reveal=True, prompt='Choose a Supporter card'),
        ),
        Attack(
            title='Bite',
            game_text='',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
