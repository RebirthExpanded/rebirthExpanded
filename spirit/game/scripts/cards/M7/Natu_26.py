"""Natu (M7 26 -- JP M7 026/078 ネイティ). Japanese art.

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
    guid="f49e067d-0aa7-5be3-8405-a40942491ab6",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name='Natu',
    searchable_by=['Natu', 'Basic', 'Natu'],
    subtypes=['Basic'],
    collector_number=26,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=177,
    abilities=[
        Attack(
            title='Scary Gaze',
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 30 less damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=pc.debuff_defender_attacks(30),
        ),
        Attack(
            title='Flap',
            game_text='',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
