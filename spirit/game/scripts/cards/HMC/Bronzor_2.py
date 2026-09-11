"""Bronzor (JP XY Hyper Metal Chain Deck 60 -- HMC 002/018; English print
XY - Phantom Forces 60/119).

Basic Metal Pokemon. HP 50, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Tackle  [M] 10
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="71392ca9-4ebd-5055-8602-0d94427bde93",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="HMC",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=436,
    abilities=[
        Attack(title="Tackle", game_text="",
               cost={PokemonTypes.METAL: 1}, damage=10),
    ],
)
