"""Hitmontop (M7 40 -- JP M7 040/078 カポエラー). Japanese art.

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
    guid="f7fbf814-841f-5634-81c6-99e322a045c4",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name='Hitmontop',
    searchable_by=['Hitmontop', 'Basic', 'Hitmontop'],
    subtypes=['Basic'],
    collector_number=40,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Attack(
            title='Triple Kick',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='x',
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title='Guts Fight',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.recoil_attack(20),
        ),
    ],
)
