"""Ninetales (M7 13 -- JP M7 013/078 キュウコン). Japanese art.

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
    guid="d47705cb-bdc7-56ce-a80d-8312379dc5a6",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name='Ninetales',
    searchable_by=['Ninetales', 'Stage 1', 'Ninetales'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title='Illusion',
            game_text="If you have exactly 5 cards in your hand and this Pokémon is Knocked Out, your opponent can't take any Prize cards for it.",
            passive=m7.IllusionPassive(),
        ),
        Attack(
            title='Scorch',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=m7.scorch,
        ),
    ],
)
