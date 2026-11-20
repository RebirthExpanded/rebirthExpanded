"""Revavroom (M7 61 -- JP M7 061/078 ブロロローム). Japanese art.

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
    guid="77b010e4-dde2-5946-a27e-dbe7e0d4fe28",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name",
    display_name='Revavroom',
    searchable_by=['Revavroom', 'Stage 1', 'Revavroom'],
    subtypes=['Stage 1'],
    collector_number=61,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Attack(
            title='Gas Wrap',
            game_text='',
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title='Long Drive',
            game_text="Discard all Energy from this Pokémon, and this attack also does 100 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 3},
            damage=100,
            effect=m7.long_drive,
        ),
    ],
)
