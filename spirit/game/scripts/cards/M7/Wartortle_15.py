"""Wartortle (M7 15 -- JP M7 015/078 カメール). Japanese art.

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
    guid="dd49409d-93af-5939-b5bc-2562da7f7be2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name='Wartortle',
    searchable_by=['Wartortle', 'Stage 1', 'Wartortle'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title='Bubble Beam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            effect=m7.bubble_beam_paralyze,
        ),
    ],
)
