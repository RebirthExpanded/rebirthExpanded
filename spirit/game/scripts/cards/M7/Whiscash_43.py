"""Whiscash (M7 43 -- JP M7 043/078 ナマズン). Japanese art.

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
    guid="017f3b5a-2015-58c2-a30f-a03538e7a66a",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name='Whiscash',
    searchable_by=['Whiscash', 'Stage 1', 'Whiscash'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Attack(
            title='Big Shake',
            game_text="Discard the Stadium in play. If you can't, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=m7.big_shake,
        ),
        Attack(
            title='Mud Shot',
            game_text='',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
