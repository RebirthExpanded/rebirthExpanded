"""Mega Glimmora ex (M7 54 -- JP M7 054/078 メガキラフロルex). Japanese art.

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
    guid="0f9e3b6d-de37-518a-af7a-cdcf7fefcc18",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGlimmoraex.Name",
    display_name='Mega Glimmora ex',
    searchable_by=['Mega Glimmora ex', 'Stage 1', 'ex', 'SV_Mega', 'MegaGlimmoraex'],
    subtypes=['Stage 1', 'ex', 'SV_Mega'],
    collector_number=54,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Attack(
            title='Toxic Gem',
            game_text="Put damage counters on 2 of your opponent's Pokémon until each of them has 60 HP left.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=m7.toxic_gem,
        ),
        Attack(
            title='Big Spin',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=250,
            effect=m7.big_spin,
        ),
    ],
)
