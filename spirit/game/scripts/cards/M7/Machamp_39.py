"""Machamp (M7 39 -- JP M7 039/078 カイリキー). Japanese art.

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
    guid="e7f740fe-a5da-5f8f-88f9-13a2ebf8f93f",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name='Machamp',
    searchable_by=['Machamp', 'Stage 2', 'Machamp'],
    subtypes=['Stage 2'],
    collector_number=39,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title='Trained Arm',
            game_text="Damage from this Pokémon's attacks isn't affected by Resistance or by any effects on your opponent's Active Pokémon.",
            passive=m7.TrainedArmPassive(),
        ),
        Attack(
            title='Guts Fight',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=250,
            effect=ac.recoil_attack(20),
        ),
    ],
)
