"""Inkay (SM - Forbidden Light 50/131 -- JP SM6 036/094).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, retreat 1.

  Hypnosis  [P]  Your opponent's Active Pokemon is now Asleep.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="8d9c440a-207d-5126-8235-8b324acd9945",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=['Inkay', 'Basic', 'Inkay'],
    subtypes=['Basic'],
    collector_number=86,
    set_code="HF",
    rarity=Rarities.RareHolo,
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
