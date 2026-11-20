"""Mega Garchomp Z ex (M7 67 -- JP M7 067/078 メガガブリアスZex). Japanese art.

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
    guid="94ed781f-b9c8-59ef-911c-dcd7bfdbc341",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGarchompZex.Name",
    display_name='Mega Garchomp Z ex',
    searchable_by=['Mega Garchomp Z ex', 'Stage 2', 'ex', 'SV_Mega', 'MegaGarchompZex'],
    subtypes=['Stage 2', 'ex', 'SV_Mega'],
    collector_number=67,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=360,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title='Drago Avenger',
            game_text='This attack does 30 damage for each Dragon Pokémon in your discard pile.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator='x',
            effect=ac.damage_per(m7.count_my_dragon_in_discard, 30),
        ),
        Attack(
            title='Sonic Edge',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
