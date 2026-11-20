"""Gabite (M7 66 -- JP M7 066/078 ガバイト). Japanese art.

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
    guid="c9ed10c4-5620-5176-81e1-84a2fedbba71",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name='Gabite',
    searchable_by=['Gabite', 'Stage 1', 'Gabite'],
    subtypes=['Stage 1'],
    collector_number=66,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 2 cards of your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=m7.mill_self_attack(2),
        ),
    ],
)
