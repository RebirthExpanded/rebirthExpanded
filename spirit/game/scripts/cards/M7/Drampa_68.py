"""Drampa (M7 68 -- JP M7 068/078 ジジーロン). Japanese art.

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
    guid="c43eee24-18bb-5732-b082-f2785450b4fa",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name='Drampa',
    searchable_by=['Drampa', 'Basic', 'Drampa'],
    subtypes=['Basic'],
    collector_number=68,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=780,
    abilities=[
        Attack(
            title='Power Breath',
            game_text='Search your deck for a Basic Energy card and attach it to 1 of your Dragon Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=m7.power_breath,
        ),
        Attack(
            title='Hidden Strength',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=m7.big_spin,
        ),
    ],
)
