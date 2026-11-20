"""Gible (M7 65 -- JP M7 065/078 フカマル). Japanese art.

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
    guid="c86773d1-ad5a-55cd-b2e6-0808488f03c4",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name='Gible',
    searchable_by=['Gible', 'Basic', 'Gible'],
    subtypes=['Basic'],
    collector_number=65,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=443,
    abilities=[
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top card of your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=m7.mill_self_attack(1),
        ),
    ],
)
