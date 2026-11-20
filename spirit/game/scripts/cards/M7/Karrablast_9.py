"""Karrablast (M7 9 -- JP M7 009/078 カブルモ). Japanese art.

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
    guid="ab9a7940-223b-55d6-9a40-195153177eea",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name='Karrablast',
    searchable_by=['Karrablast', 'Basic', 'Karrablast'],
    subtypes=['Basic'],
    collector_number=9,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Attack(
            title='Gnaw',
            game_text='',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
