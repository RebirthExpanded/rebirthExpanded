"""Hattrem (M7 35 -- JP M7 035/078 テブリム). Japanese art.

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
    guid="730cf1cd-a58d-53bd-9629-cb91c0b75561",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    display_name='Hattrem',
    searchable_by=['Hattrem', 'Stage 1', 'Hattrem'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    family_id=856,
    abilities=[
        Attack(
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='x',
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
    ],
)
