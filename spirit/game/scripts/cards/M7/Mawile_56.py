"""Mawile (M7 56 -- JP M7 056/078 クチート). Japanese art.

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
    guid="63e4d8b4-8dda-5dd0-bf48-c20f521a6457",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name='Mawile',
    searchable_by=['Mawile', 'Basic', 'Mawile'],
    subtypes=['Basic'],
    collector_number=56,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=303,
    abilities=[
        Attack(
            title='Big Jaw',
            game_text="This attack does 30 damage for each card in your opponent's hand.",
            cost={PokemonTypes.METAL: 3},
            damage=30,
            damage_operator='x',
            effect=ac.damage_per(ac.count_hand('opponent'), 30),
        ),
    ],
)
