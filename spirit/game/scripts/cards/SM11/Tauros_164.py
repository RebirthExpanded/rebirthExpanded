"""Tauros (SM - Unified Minds 164/236 -- JP SM11 072/094).

Basic Colorless Pokemon. HP 110, weakness Fighting x2, retreat 1.

  Call for Family   [C]      Search your deck for a Basic Pokemon and put it
                             onto your Bench. Then, shuffle your deck.
  Berserker Tackle  [CC] 60  This Pokemon does 10 damage to itself.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="75891540-e42c-5c9f-bf6f-3f442b43a540",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=['Tauros', 'Basic', 'Tauros'],
    subtypes=['Basic'],
    collector_number=164,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(title="Call for Family", game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=search_to_bench(count=1)),
        Attack(title="Berserker Tackle", game_text="This Pokémon does 10 damage to itself.",
               cost={PokemonTypes.COLORLESS: 2}, damage=60,
               effect=recoil_attack(10)),
    ],
)
