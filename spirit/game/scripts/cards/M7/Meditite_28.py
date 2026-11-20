"""Meditite (M7 28 -- JP M7 028/078 アサナン). Japanese art.

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
    guid="83c56d20-a640-54a2-ab35-51fcedc86d8d",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    display_name='Meditite',
    searchable_by=['Meditite', 'Basic', 'Meditite'],
    subtypes=['Basic'],
    collector_number=28,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=307,
    abilities=[
        Attack(
            title='Chop',
            game_text='',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
