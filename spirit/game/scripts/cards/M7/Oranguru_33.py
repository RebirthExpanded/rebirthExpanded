"""Oranguru (M7 33 -- JP M7 033/078 ヤレユータン). Japanese art.

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
    guid="2f0f4efb-356e-5c25-bf47-670c60042d6a",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name='Oranguru',
    searchable_by=['Oranguru', 'Basic', 'Oranguru'],
    subtypes=['Basic'],
    collector_number=33,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=765,
    abilities=[
        Attack(
            title='Slap',
            game_text='',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Sage's Command",
            game_text='This attack does 60 damage for each Mega Evolution Pokémon ex on your Bench.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='x',
            effect=ac.damage_per(m7.count_my_bench_mega_ex, 60),
        ),
    ],
)
