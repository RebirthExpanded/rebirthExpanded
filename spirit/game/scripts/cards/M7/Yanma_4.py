"""Yanma (M7 4 -- JP M7 004/078 ヤンヤンマ). Japanese art.

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
    guid="b8d08aba-2ba5-5719-a05b-c886e63945a4",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name='Yanma',
    searchable_by=['Yanma', 'Basic', 'Yanma'],
    subtypes=['Basic'],
    collector_number=4,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=193,
    abilities=[
        Attack(
            title='Tackle',
            game_text='',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Gust',
            game_text='',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
