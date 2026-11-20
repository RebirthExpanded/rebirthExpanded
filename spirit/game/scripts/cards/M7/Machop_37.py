"""Machop (M7 37 -- JP M7 037/078 ワンリキー). Japanese art.

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
    guid="f2bcc8fe-55b2-5a9e-a9e3-950d80bbe1fc",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    display_name='Machop',
    searchable_by=['Machop', 'Basic', 'Machop'],
    subtypes=['Basic'],
    collector_number=37,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=66,
    abilities=[
        Attack(
            title='Punch',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
