"""Glimmet (M7 53 -- JP M7 053/078 キラーメ). Japanese art.

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
    guid="7cb3e00b-892e-557a-a983-cb2a34637766",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name='Glimmet',
    searchable_by=['Glimmet', 'Basic', 'Glimmet'],
    subtypes=['Basic'],
    collector_number=53,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=969,
    abilities=[
        Attack(
            title='Poison Spray',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=m7.poison_claws,
        ),
    ],
)
