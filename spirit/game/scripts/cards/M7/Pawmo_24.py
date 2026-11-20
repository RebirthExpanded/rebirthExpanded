"""Pawmo (M7 24 -- JP M7 024/078 パモット). Japanese art.

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
    guid="56164b7a-0891-5fb5-b756-9dbef531e08c",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    display_name='Pawmo',
    searchable_by=['Pawmo', 'Stage 1', 'Pawmo'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    family_id=921,
    abilities=[
        Attack(
            title='Assault Bolt',
            game_text="If your opponent's Active Pokémon has a Pokémon Tool attached, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            damage_operator='+',
            effect=ac.bonus_if(ac.active_is(ac.has_tool), 80),
        ),
    ],
)
