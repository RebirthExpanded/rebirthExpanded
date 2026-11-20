"""Togedemaru ex (M7 59 -- JP M7 059/078 トゲデマルex). Japanese art.

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
    guid="b7f179bb-df30-5c95-8a55-98cf8ae61e51",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaruex.Name",
    display_name='Togedemaru ex',
    searchable_by=['Togedemaru ex', 'Basic', 'ex', 'Togedemaruex'],
    subtypes=['Basic', 'ex'],
    collector_number=59,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=777,
    abilities=[
        Ability(
            title='Dual Type',
            game_text='As long as this Pokémon is in play, it is Lightning and Metal type.',
            passive=m7.DualTypePassive(),
        ),
        Attack(
            title='All-Out Needle',
            game_text="During your next turn, this Pokémon's All-Out Needle does 60 damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=m7.all_out_needle,
        ),
    ],
)
