"""Yanmega (M7 5 -- JP M7 005/078 メガヤンマ). Japanese art.

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
    guid="17ada0b8-1807-5b6f-9062-aa144632d2cf",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name='Yanmega',
    searchable_by=['Yanmega', 'Stage 1', 'Yanmega'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Attack(
            title='Damage Beat',
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='x',
            effect=ac.damage_per(ac.damage_counters_on('defender'), 20),
        ),
        Attack(
            title='Bug Buzz',
            game_text='',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
