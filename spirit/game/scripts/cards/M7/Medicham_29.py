"""Medicham (M7 29 -- JP M7 029/078 チャーレム). Japanese art.

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
    guid="d9fc13c2-a8ef-5db1-9794-a7de2f9dcb31",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name='Medicham',
    searchable_by=['Medicham', 'Stage 1', 'Medicham'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title='Yoga Power',
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=m7.yoga_power,
        ),
        Attack(
            title='Guts Fight',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=ac.recoil_attack(20),
        ),
    ],
)
