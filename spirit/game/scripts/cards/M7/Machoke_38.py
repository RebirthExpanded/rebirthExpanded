"""Machoke (M7 38 -- JP M7 038/078 ゴーリキー). Japanese art.

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
    guid="2cde7aa6-9b59-5b06-b4c2-c58417284368",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name='Machoke',
    searchable_by=['Machoke', 'Stage 1', 'Machoke'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title='Fist',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title='Slam',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
