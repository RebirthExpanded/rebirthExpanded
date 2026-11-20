"""Vibrava (M7 63 -- JP M7 063/078 ビブラーバ). Japanese art.

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
    guid="a17354f6-9de5-5d94-ab7f-0f17cd9fb86c",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name='Vibrava',
    searchable_by=['Vibrava', 'Stage 1', 'Vibrava'],
    subtypes=['Stage 1'],
    collector_number=63,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=328,
    abilities=[
        Ability(
            title='Quivering Wings',
            game_text='Once during your turn, if this Pokémon is in your hand, you may use this Ability. If you do, discard this card, then look at the top card of your deck and put it back.',
            activation=Activations.ONCE_PER_TURN,
            usable_from='hand',
            condition=m7.quivering_wings_condition,
            effect=m7.quivering_wings,
        ),
        Attack(
            title='Sand Spray',
            game_text='',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1},
            damage=60,
        ),
    ],
)
