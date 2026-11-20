"""Flygon (M7 64 -- JP M7 064/078 フライゴン). Japanese art.

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
    guid="f77e7c83-6f28-5b08-b737-1ac9ea3d5aa8",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name='Flygon',
    searchable_by=['Flygon', 'Stage 2', 'Flygon'],
    subtypes=['Stage 2'],
    collector_number=64,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Attack(
            title='Desert Wind',
            game_text="You may choose 2 Energy attached to your opponent's Active Pokémon and shuffle them into your opponent's deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=m7.desert_wind,
        ),
        Attack(
            title='Speed Flight',
            game_text='',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)
