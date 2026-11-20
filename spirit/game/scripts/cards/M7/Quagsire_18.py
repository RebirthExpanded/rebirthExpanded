"""Quagsire (M7 18 -- JP M7 018/078 ヌオー). Japanese art.

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
    guid="fc71d2ff-414a-54ed-867f-d8b1618eb4a5",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name='Quagsire',
    searchable_by=['Quagsire', 'Stage 1', 'Quagsire'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title='Hot-Blooded Head',
            game_text="You may reveal a Maxi's Passion card from your hand. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator='+',
            effect=m7.hot_blooded_head,
        ),
    ],
)
