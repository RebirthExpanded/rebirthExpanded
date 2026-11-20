"""Wooper (M7 17 -- JP M7 017/078 ウパー). Japanese art.

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
    guid="78f27937-e38a-5f1f-921e-d313b455cef2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name='Wooper',
    searchable_by=['Wooper', 'Basic', 'Wooper'],
    subtypes=['Basic'],
    collector_number=17,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=194,
    abilities=[
        Attack(
            title='Headbutt',
            game_text='',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
