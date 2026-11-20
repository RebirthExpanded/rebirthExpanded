"""Oricorio (M7 22 -- JP M7 022/078 オドリドリ). Japanese art.

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
    guid="fb4505d3-95a5-52be-a55c-3a99dcc12234",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name='Oricorio',
    searchable_by=['Oricorio', 'Basic', 'Oricorio'],
    subtypes=['Basic'],
    collector_number=22,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=741,
    abilities=[
        Attack(
            title='Welcoming Dance',
            game_text="Look at your opponent's hand and put up to 3 Basic Pokémon you find there onto their Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=m7.welcoming_dance,
        ),
        Attack(
            title='Zap',
            game_text='',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)
