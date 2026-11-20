"""Riolu (M7 44 -- JP M7 044/078 リオル). Japanese art.

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
    guid="fe32c79c-b2c1-597f-87c3-4fa475c80a1c",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name='Riolu',
    searchable_by=['Riolu', 'Basic', 'Riolu'],
    subtypes=['Basic'],
    collector_number=44,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Attack(
            title='Back Kick',
            game_text='',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
