"""Dragonair (SM - Unified Minds 150/236 -- JP SM11 056/094).

Stage 1 Dragon Pokemon, evolves from Dratini. HP 100, weakness Fairy x2,
retreat 2.

  Tail Whap              [C] 20
  Destructive Whirlpool  [WLCC] 70  Discard an Energy from your opponent's
                                    Active Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="a7a6334f-5ed9-5c26-b09b-0a3b33c2f71f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=['Dragonair', 'Stage 1', 'Dragonair'],
    subtypes=['Stage 1'],
    collector_number=150,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(title="Tail Whap", game_text="",
               cost={PokemonTypes.COLORLESS: 1}, damage=20),
        Attack(title="Destructive Whirlpool", game_text="Discard an Energy from your opponent's Active Pokémon.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=70,
               effect=discard_opponent_energy_attack(1)),
    ],
)
