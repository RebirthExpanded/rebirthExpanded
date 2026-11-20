"""Malamar (M7 52 -- JP M7 052/078 カラマネロ). Japanese art.

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
    guid="8e38bd71-88ec-5491-a61c-c7de16e443ad",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name='Malamar',
    searchable_by=['Malamar', 'Stage 1', 'Malamar'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title='Skill Control',
            game_text="Choose 1 of the attacks of your opponent's Active Mega Evolution Pokémon ex and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=m7.skill_control,
        ),
        Attack(
            title='Smack Down',
            game_text='',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
