"""Mega Absol Z ex (M7 30 -- JP M7 030/078 メガアブソルZex). Japanese art.

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
    guid="82ec60ad-a1ad-56b6-9f8c-a2ca02ce01e2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAbsolZex.Name",
    display_name='Mega Absol Z ex',
    searchable_by=['Mega Absol Z ex', 'Basic', 'ex', 'SV_Mega', 'MegaAbsolZex'],
    subtypes=['Basic', 'ex', 'SV_Mega'],
    collector_number=30,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=359,
    abilities=[
        Attack(
            title='Bloody Fear',
            game_text="During your opponent's next turn, they can't play any Special Energy or Stadium cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=m7.bloody_fear,
        ),
    ],
)
