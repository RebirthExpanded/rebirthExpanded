"""Gimmighoul (SV - Paradox Rift 87/182 -- JP SV3a 020/062).

Basic Psychic Pokemon. HP 50, weakness Darkness x2, resistance Fighting
-30, retreat 1.

  Call for Family    [C]     Search your deck for a Basic Pokemon and put
                             it onto your Bench. Then, shuffle your deck.
  Corkscrew Punch    [CC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="203a7232-c2ef-5747-ba55-ca3cb8c808c0",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=999,
    regulation_mark="G",
    abilities=[
        Attack(title="Call for Family",
               game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0, effect=search_to_bench(count=1)),
        Attack(title="Corkscrew Punch", game_text="", cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
