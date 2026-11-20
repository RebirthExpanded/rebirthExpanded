"""Escavalier (M7 58 -- JP M7 058/078 シュバルゴ). Japanese art.

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
    guid="03fcf7a8-7113-5468-b651-4a05cd3cf4db",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name='Escavalier',
    searchable_by=['Escavalier', 'Stage 1', 'Escavalier'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title='Cavalry Lance',
            game_text="This attack does 50 damage for each of your opponent's Basic Pokémon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=ac.damage_per(m7.count_opponent_basics, 50),
        ),
        Attack(
            title='Iron Lance',
            game_text='',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
