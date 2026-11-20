"""Accelgor (M7 11 -- JP M7 011/078 アギルダー). Japanese art.

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
    guid="b326f2ce-a0a7-5155-9013-f9216a96bddd",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name='Accelgor',
    searchable_by=['Accelgor', 'Stage 1', 'Accelgor'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title='Stealthy Slash',
            game_text="This attack does 50 damage for each of your opponent's Evolution Pokémon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=ac.damage_per(m7.count_opponent_evolved, 50),
        ),
        Attack(
            title='Raid',
            game_text='',
            cost={PokemonTypes.GRASS: 2},
            damage=70,
        ),
    ],
)
