"""Trapinch (M7 41 -- JP M7 041/078 ナックラー). Japanese art.

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
    guid="f8c9dc97-ee7f-5463-8694-9eade23c89e0",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name='Trapinch',
    searchable_by=['Trapinch', 'Basic', 'Trapinch'],
    subtypes=['Basic'],
    collector_number=41,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title='Mountain Munch',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.mill_attack(1),
        ),
    ],
)
