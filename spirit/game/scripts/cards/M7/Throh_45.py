"""Throh (M7 45 -- JP M7 045/078 ナゲキ). Japanese art.

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
    guid="8da05f45-26c4-52dc-8128-f8cb57bc7de2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name='Throh',
    searchable_by=['Throh', 'Basic', 'Throh'],
    subtypes=['Basic'],
    collector_number=45,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title='Circle Throw',
            game_text="Switch your opponent's Active Pokémon with 1 of their Benched Pokémon. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=m7.circle_throw,
        ),
        Attack(
            title='Guts Fight',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=ac.recoil_attack(20),
        ),
    ],
)
