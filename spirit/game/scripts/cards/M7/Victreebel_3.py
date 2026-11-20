"""Victreebel (M7 3 -- JP M7 003/078 ウツボット). Japanese art.

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
    guid="9ca7e6c5-7ae8-59ff-8dfe-8992d445bb60",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name='Victreebel',
    searchable_by=['Victreebel', 'Stage 2', 'Victreebel'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title='Acid Trap',
            game_text="Once during your turn, if you have a Stadium in play, you may make your opponent's Active Pokémon Poisoned and Burned.",
            activation=Activations.ONCE_PER_TURN,
            condition=m7.acid_trap_condition,
            effect=m7.acid_trap,
        ),
        Attack(
            title='Leaf Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=su.heal_attack(30),
        ),
    ],
)
