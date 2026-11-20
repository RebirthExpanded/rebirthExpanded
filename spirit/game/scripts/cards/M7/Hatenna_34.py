"""Hatenna (M7 34 -- JP M7 034/078 ミブリム). Japanese art.

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
    guid="2a8e33b9-a21a-5884-9076-7a153dc06982",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    display_name='Hatenna',
    searchable_by=['Hatenna', 'Basic', 'Hatenna'],
    subtypes=['Basic'],
    collector_number=34,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=856,
    abilities=[
        Attack(
            title='Future Sight',
            game_text="Look at the top 3 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=m7.future_sight,
        ),
    ],
)
