"""Pawmot (M7 25 -- JP M7 025/078 パーモット). Japanese art.

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
    guid="3e2f89c9-4dec-558f-8f77-7354aa405597",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name='Pawmot',
    searchable_by=['Pawmot', 'Stage 2', 'Pawmot'],
    subtypes=['Stage 2'],
    collector_number=25,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Ability(
            title='Double Combo',
            game_text="This Pokémon may attack twice in a row. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)",
            passive=AttackTwicePassive(),
        ),
        Attack(
            title='Mach Bolt',
            game_text='',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=100,
        ),
    ],
)
