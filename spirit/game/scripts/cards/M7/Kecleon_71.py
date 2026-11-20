"""Kecleon (M7 71 -- JP M7 071/078 カクレオン). Japanese art.

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
    guid="dcc3a041-dbf3-560b-9798-5051dbacf466",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name='Kecleon',
    searchable_by=['Kecleon', 'Basic', 'Kecleon'],
    subtypes=['Basic'],
    collector_number=71,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title='Synchro Body',
            game_text='As long as this Pokémon is in play, in addition to its own type, it is the same type as each of your Benched Pokémon.',
            passive=m7.SynchroBodyPassive(),
        ),
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 60 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=ac.flip_bonus(60),
        ),
    ],
)
