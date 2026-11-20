"""Shelmet (M7 10 -- JP M7 010/078 チョボマキ). Japanese art.

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
    guid="0c4cc0d2-cb3b-55c2-97ce-524f87d0ec0e",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name='Shelmet',
    searchable_by=['Shelmet', 'Basic', 'Shelmet'],
    subtypes=['Basic'],
    collector_number=10,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
