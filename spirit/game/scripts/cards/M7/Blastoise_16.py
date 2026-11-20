"""Blastoise (M7 16 -- JP M7 016/078 カメックス). Japanese art.

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
    guid="26678014-6974-55c5-bf8e-f49af403ada2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name='Blastoise',
    searchable_by=['Blastoise', 'Stage 2', 'Blastoise'],
    subtypes=['Stage 2'],
    collector_number=16,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title='Water Pump',
            game_text="Attacks used by your Water Pokémon do 30 more damage to your opponent's Benched Pokémon. The effect of Water Pump doesn't stack.",
            passive=m7.WaterPumpPassive(),
        ),
        Attack(
            title='Heavy Splash',
            game_text='',
            cost={PokemonTypes.WATER: 3},
            damage=140,
        ),
    ],
)
