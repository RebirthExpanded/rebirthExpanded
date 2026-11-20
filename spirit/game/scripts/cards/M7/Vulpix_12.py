"""Vulpix (M7 12 -- JP M7 012/078 ロコン). Japanese art.

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
    guid="9bd88a62-52f1-51a3-b580-4b311b162ca1",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name='Vulpix',
    searchable_by=['Vulpix', 'Basic', 'Vulpix'],
    subtypes=['Basic'],
    collector_number=12,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title='Continuous Steps',
            game_text='Flip a coin until you get tails. This attack does 20 damage for each heads.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator='x',
            effect=ac.flip_damage(per_heads=20, until_tails=True),
        ),
    ],
)
