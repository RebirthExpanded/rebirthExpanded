"""Kubfu (M7 48 -- JP M7 048/078 ダクマ). Japanese art.

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
    guid="39b12d40-09c9-5601-9917-16d2c129abe1",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kubfu.Name",
    display_name='Kubfu',
    searchable_by=['Kubfu', 'Basic', 'Kubfu'],
    subtypes=['Basic'],
    collector_number=48,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=891,
    abilities=[
        Attack(
            title='Jab',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
