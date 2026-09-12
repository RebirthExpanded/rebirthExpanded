"""Archen (SM - Unified Minds 120/236 -- JP SM11 051/094, the art here).

Stage 1 Fighting Pokemon, evolves from Unidentified Fossil. HP 80,
weakness Lightning x2, resistance Fighting -20, retreat 1.

  Endeavor [C] 20+  Flip 2 coins. This attack does 20 more damage for
                    each heads.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="aa9f297a-4e9b-5cd1-b7bb-4ba54c721fc5",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    display_name="Archen",
    searchable_by=["Archen", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=566,
    abilities=[
        Attack(title="Endeavor",
               game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
               cost={PokemonTypes.COLORLESS: 1},
               damage=20, damage_operator="+",
               effect=flip_damage(coins=2, base=20, bonus_per_heads=20)),
    ],
)
