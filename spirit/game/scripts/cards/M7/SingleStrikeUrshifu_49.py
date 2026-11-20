"""Single Strike Urshifu (M7 49 -- JP M7 049/078 いちげきウーラオス). Japanese art.

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
    guid="404a4729-80ad-5899-97a6-ada968e75c31",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifu.Name",
    display_name='Single Strike Urshifu',
    searchable_by=['Single Strike Urshifu', 'Stage 1', 'SingleStrikeUrshifu'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kubfu.Name",
    family_id=891,
    abilities=[
        Attack(
            title='Dark Strike Combo',
            game_text='You may discard a Darkness Energy from this Pokémon. If you do, this attack does 140 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator='+',
            effect=m7.dark_strike_combo,
        ),
    ],
)
