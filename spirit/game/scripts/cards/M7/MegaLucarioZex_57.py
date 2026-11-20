"""Mega Lucario Z ex (M7 57 -- JP M7 057/078 メガルカリオZex). Japanese art.

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
    guid="e741d8a6-7f69-5e47-96d2-da11f9617b44",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLucarioZex.Name",
    display_name='Mega Lucario Z ex',
    searchable_by=['Mega Lucario Z ex', 'Stage 1', 'ex', 'SV_Mega', 'MegaLucarioZex'],
    subtypes=['Stage 1', 'ex', 'SV_Mega'],
    collector_number=57,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title='Aura Seeker',
            game_text='Once during your turn, if this Pokémon is in the Active Spot, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.',
            activation=Activations.ONCE_PER_TURN,
            condition=m7.aura_seeker_condition,
            effect=m7.aura_seeker,
        ),
        Attack(
            title='Dancing Fist',
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            damage_operator='+',
            effect=m7.dancing_fist,
        ),
    ],
)
