"""Floatzel ex (M7 20 -- JP M7 020/078 フローゼルex). Japanese art.

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
    guid="9f245c64-f6e4-5064-b0ec-abb80e3e3d0e",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzelex.Name",
    display_name='Floatzel ex',
    searchable_by=['Floatzel ex', 'Stage 1', 'ex', 'Floatzelex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=20,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title='Hustle Screw',
            game_text="Reveal any number of Maxi's Passion cards from your hand. This attack does 100 more damage for each card you revealed this way. Then, shuffle the revealed cards into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=m7.hustle_screw,
        ),
        Attack(
            title='Waterfall',
            game_text='',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
    ],
)
