"""Sceptile ex (M7 8 -- JP M7 008/078 ジュカインex). Japanese art.

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
    guid="1b746758-e104-57b2-b252-023326ada66a",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptileex.Name",
    display_name='Sceptile ex',
    searchable_by=['Sceptile ex', 'Stage 2', 'ex', 'Sceptileex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=8,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Attack(
            title='Poison Claws',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=m7.poison_claws,
        ),
        Attack(
            title='Assassin Blade',
            game_text="This attack does 50 more damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 2},
            damage=160,
            damage_operator='+',
            effect=m7.assassin_blade,
        ),
    ],
)
