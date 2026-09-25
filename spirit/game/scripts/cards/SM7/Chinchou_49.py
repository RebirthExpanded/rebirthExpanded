"""Chinchou (SM - Celestial Storm 49/168 -- JP SM6b 020/066).

Basic Lightning Pokemon. HP 60, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Pound  [C] 10
  Spark  [LC] 10  This attack does 10 damage to 2 of your opponent's Benched
                  Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="ae0c0844-1d07-550b-8b39-4bc6ca3c3bd7",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=['Chinchou', 'Basic', 'Chinchou'],
    subtypes=['Basic'],
    collector_number=49,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=170,
    abilities=[
        Attack(title="Pound", game_text="",
               cost={PokemonTypes.COLORLESS: 1}, damage=10),
        Attack(title="Spark", game_text="This attack does 10 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=10,
               effect=snipe_attack(10, pool="bench", count=2, also_base=True)),
    ],
)
