"""Varoom (M7 60 -- JP M7 060/078 ブロロン). Japanese art.

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
    guid="6e39e555-7b6a-5967-90c4-2e2e73d7cd8a",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name='Varoom',
    searchable_by=['Varoom', 'Basic', 'Varoom'],
    subtypes=['Basic'],
    collector_number=60,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=965,
    abilities=[
        Attack(
            title='Stomp',
            game_text='',
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)
