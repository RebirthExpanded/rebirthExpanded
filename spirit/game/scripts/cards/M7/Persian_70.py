"""Persian (M7 70 -- JP M7 070/078 ペルシアン). Japanese art.

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
    guid="8da85b21-a03b-5293-b61a-21dd5e0d21a3",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name='Persian',
    searchable_by=['Persian', 'Stage 1', 'Persian'],
    subtypes=['Stage 1'],
    collector_number=70,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title='Big Coin Bonanza',
            game_text='Once during your turn, if you have 2 or more Pokémon in play with the attack Pay Day, you may draw 2 cards.',
            activation=Activations.ONCE_PER_TURN,
            condition=m7.big_coin_bonanza_condition,
            effect=m7.big_coin_bonanza,
        ),
        Attack(
            title='Greedy Slash',
            game_text='This attack does 20 damage for each card in your hand.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='x',
            effect=ac.damage_per(ac.count_hand('mine'), 20),
        ),
    ],
)
