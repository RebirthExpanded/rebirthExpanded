"""Treecko (M7 6 -- JP M7 006/078 キモリ). Japanese art.

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
    guid="fa13d34f-d914-57f8-a7a7-70d0335356e6",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name='Treecko',
    searchable_by=['Treecko', 'Basic', 'Treecko'],
    subtypes=['Basic'],
    collector_number=6,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=252,
    abilities=[
        Attack(
            title='Hide',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title='Cut',
            game_text='',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
