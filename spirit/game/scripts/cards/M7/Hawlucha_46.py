"""Hawlucha (M7 46 -- JP M7 046/078 ルチャブル). Japanese art.

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
    guid="156555e3-1320-5703-affd-151caa0735e1",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name='Hawlucha',
    searchable_by=['Hawlucha', 'Basic', 'Hawlucha'],
    subtypes=['Basic'],
    collector_number=46,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Ability(
            title='Surging Cheer',
            game_text='As long as this Pokémon is in play, the Guts Fight attacks of your Pokémon cost [C] less.',
            passive=m7.GutsFightDiscountPassive(),
        ),
        Attack(
            title='Smack',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
