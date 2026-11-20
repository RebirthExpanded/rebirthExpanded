"""Regigigas (M7 73 -- JP M7 073/078 レジギガス). Japanese art.

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
    guid="d41d92fc-2ff9-5970-8a23-f1c22b6625e8",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name='Regigigas',
    searchable_by=['Regigigas', 'Basic', 'Regigigas'],
    subtypes=['Basic'],
    collector_number=73,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title='Destructive Hammer',
            game_text='You may discard up to 10 cards from the top of your deck. This attack does 10 more damage for each card you discarded this way.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator='+',
            effect=m7.destructive_hammer,
        ),
    ],
)
