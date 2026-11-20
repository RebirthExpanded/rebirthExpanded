"""Hatterene (M7 36 -- JP M7 036/078 ブリムオン). Japanese art.

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
    guid="d5146903-4a08-508f-9f5e-8ea26ed57e56",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatterene.Name",
    display_name='Hatterene',
    searchable_by=['Hatterene', 'Stage 2', 'Hatterene'],
    subtypes=['Stage 2'],
    collector_number=36,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    family_id=856,
    abilities=[
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=m7.bewilder,
        ),
        Attack(
            title='Magic Tentacle',
            game_text="Discard the top card of each player's deck. This attack does 100 more damage for each Trainer card discarded this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=100,
            damage_operator='+',
            effect=m7.magic_tentacle,
        ),
    ],
)
