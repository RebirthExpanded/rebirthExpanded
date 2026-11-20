"""Grovyle (M7 7 -- JP M7 007/078 ジュプトル). Japanese art.

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
    guid="68f07a04-a539-522e-96b9-1d439534107d",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name='Grovyle',
    searchable_by=['Grovyle', 'Stage 1', 'Grovyle'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=252,
    abilities=[
        Attack(
            title='Solar Cutter',
            game_text='',
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)
