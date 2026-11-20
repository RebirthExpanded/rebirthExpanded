"""Meowth (M7 69 -- JP M7 069/078 ニャース). Japanese art.

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
    guid="019e2266-66c1-5a2e-9ad9-e890f1035021",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name='Meowth',
    searchable_by=['Meowth', 'Basic', 'Meowth'],
    subtypes=['Basic'],
    collector_number=69,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title='Pay Day',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.draw_attack(1),
        ),
        Attack(
            title='Scratch',
            game_text='',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
