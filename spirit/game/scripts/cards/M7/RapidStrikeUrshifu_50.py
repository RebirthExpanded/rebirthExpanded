"""Rapid Strike Urshifu (M7 50 -- JP M7 050/078 れんげきウーラオス). Japanese art.

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
    guid="fb0c8a4c-5b63-5a94-8056-2fa79025b94e",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifu.Name",
    display_name='Rapid Strike Urshifu',
    searchable_by=['Rapid Strike Urshifu', 'Stage 1', 'RapidStrikeUrshifu'],
    subtypes=['Stage 1'],
    collector_number=50,
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
            title='Torrential Flurry',
            game_text="You may discard a Water Energy from this Pokémon. If you do, this attack also does 40 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=m7.torrential_flurry,
        ),
    ],
)
