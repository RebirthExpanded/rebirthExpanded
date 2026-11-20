"""Orthworm (M7 62 -- JP M7 062/078 ミミズズ). Japanese art.

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
    guid="26ff9820-3c9c-50cc-9a95-12b9cb746512",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name",
    display_name='Orthworm',
    searchable_by=['Orthworm', 'Basic', 'Orthworm'],
    subtypes=['Basic'],
    collector_number=62,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Attack(
            title='Burrow and Refuel',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon. Then, attach a Basic Metal Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.METAL: 1},
            effect=m7.burrow_and_refuel,
        ),
        Attack(
            title='Smash Head',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 3},
            damage=130,
            effect=m7.smash_head,
        ),
    ],
)
