"""Ting-Lu (M7 55 -- JP M7 055/078 ディンルー). Japanese art.

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
    guid="c4e48072-30dd-5e4c-b667-ccc427b5aabd",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name",
    display_name='Ting-Lu',
    searchable_by=['Ting-Lu', 'Basic', 'TingLu'],
    subtypes=['Basic'],
    collector_number=55,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Attack(
            title='Crush',
            game_text='',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
        Attack(
            title='Heavy Bomber',
            game_text="This attack does 50 less damage for each Energy in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=250,
            damage_operator='-',
            effect=m7.heavy_bomber,
        ),
    ],
)
