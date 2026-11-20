"""Barboach (M7 42 -- JP M7 042/078 ドジョッチ). Japanese art.

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
    guid="0ba9c54b-55c4-5743-8a73-a35fa73fc6af",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    display_name='Barboach',
    searchable_by=['Barboach', 'Basic', 'Barboach'],
    subtypes=['Basic'],
    collector_number=42,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=339,
    abilities=[
        Attack(
            title='Splash About',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
