"""Squirtle (M7 14 -- JP M7 014/078 ゼニガメ). Japanese art.

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
    guid="725fb0c8-669f-5e13-a52f-9b18ba07a078",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name='Squirtle',
    searchable_by=['Squirtle', 'Basic', 'Squirtle'],
    subtypes=['Basic'],
    collector_number=14,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=7,
    abilities=[
        Attack(
            title='Water Sprinkle',
            game_text="This attack does 10 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=ac.snipe_attack(10, pool='any'),
        ),
    ],
)
