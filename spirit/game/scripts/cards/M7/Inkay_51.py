"""Inkay (M7 51 -- JP M7 051/078 マーイーカ). Japanese art.

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
    guid="bb1a9d0a-23ce-5cd9-bfc9-20455cb9834a",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name='Inkay',
    searchable_by=['Inkay', 'Basic', 'Inkay'],
    subtypes=['Basic'],
    collector_number=51,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title='Peck',
            game_text='',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Tackle',
            game_text='',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
