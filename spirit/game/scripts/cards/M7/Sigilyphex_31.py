"""Sigilyph ex (M7 31 -- JP M7 031/078 シンボラーex). Japanese art.

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
    guid="e0f473df-98d2-5332-a936-b82a0fbbecb2",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyphex.Name",
    display_name='Sigilyph ex',
    searchable_by=['Sigilyph ex', 'Basic', 'ex', 'Sigilyphex'],
    subtypes=['Basic', 'ex'],
    collector_number=31,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=561,
    abilities=[
        Ability(
            title='Mega Protector',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Mega Evolution Pokémon ex.",
            passive=m7.MegaProtectorPassive(),
        ),
        Attack(
            title='Power Cyclone',
            game_text='Move an Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=m7.power_cyclone,
        ),
    ],
)
