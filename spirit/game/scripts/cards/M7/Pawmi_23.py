"""Pawmi (M7 23 -- JP M7 023/078 パモ). Japanese art.

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
    guid="e024cffc-16f8-5cdb-ab89-6664ae1d0785",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    display_name='Pawmi',
    searchable_by=['Pawmi', 'Basic', 'Pawmi'],
    subtypes=['Basic'],
    collector_number=23,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=921,
    abilities=[
        Attack(
            title='Quick Draw',
            game_text='Draw a card.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            effect=su.draw_attack(1),
        ),
    ],
)
