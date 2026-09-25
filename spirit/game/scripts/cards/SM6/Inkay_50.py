"""Inkay (SM - Forbidden Light 50/131 -- JP SM6 036/094).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, retreat 1.

  Hypnosis  [P]  Your opponent's Active Pokemon is now Asleep.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="e314cacc-0ae0-5cc4-bfc5-98986cba59ef",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=['Inkay', 'Basic', 'Inkay'],
    subtypes=['Basic'],
    collector_number=50,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=686,
    abilities=[
        Attack(title="Hypnosis", game_text="Your opponent's Active Pokémon is now Asleep.",
               cost={PokemonTypes.PSYCHIC: 1}, damage=0,
               effect=condition_attack(SpecialConditions.ASLEEP)),
    ],
)
