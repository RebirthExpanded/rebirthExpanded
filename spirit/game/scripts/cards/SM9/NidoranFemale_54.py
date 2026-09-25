"""Nidoran♀ (SM - Team Up 54/181 -- JP SM9 039/095).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, retreat 1.

  Call for Family  [C]     Search your deck for a Basic Pokemon and put it
                           onto your Bench. Then, shuffle your deck.
  Scratch          [CC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="15fc1d9a-c394-58c2-97a5-7f12da94b964",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    display_name="Nidoran♀",
    searchable_by=["Nidoran♀", "Nidoran", "Basic", "NidoranFemale"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(title="Call for Family",
               game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=search_to_bench(count=1)),
        Attack(title="Scratch", game_text="", cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
