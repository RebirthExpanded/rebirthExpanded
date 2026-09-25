"""Mesprit (SM - Unified Minds 84/236 -- JP SM10b 030/054).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, retreat 1.

  First Contact  [P]     Search your deck for up to 3 Basic Pokemon and put
                         them onto your Bench. Then, shuffle your deck.
  Mumble         [P] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="1c3e5a32-5465-5a88-8296-4df92862f3b7",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    display_name="Mesprit",
    searchable_by=['Mesprit', 'Basic', 'Mesprit'],
    subtypes=['Basic'],
    collector_number=84,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=481,
    abilities=[
        Attack(title="First Contact", game_text="Search your deck for up to 3 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
               cost={PokemonTypes.PSYCHIC: 1}, damage=0,
               effect=search_to_bench(count=3)),
        Attack(title="Mumble", game_text="",
               cost={PokemonTypes.PSYCHIC: 1}, damage=20),
    ],
)
