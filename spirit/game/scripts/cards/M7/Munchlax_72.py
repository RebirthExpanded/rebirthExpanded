"""Munchlax (M7 72 -- JP M7 072/078 ゴンベ). Japanese art.

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
    guid="33a4b391-94b9-58d6-9a28-d03c65a6a9e4",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munchlax.Name",
    display_name='Munchlax',
    searchable_by=['Munchlax', 'Basic', 'Munchlax'],
    subtypes=['Basic'],
    collector_number=72,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title='Stomping March',
            game_text='Search your deck for up to 3 Pokémon with a Retreat Cost of exactly 4, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={},
            effect=m7.stomping_march,
        ),
    ],
)
