"""Skarmory (JP XY Hyper Metal Chain Deck 60 -- HMC 001/018; English print
XY - Phantom Forces 59/119).

Basic Metal Pokemon. HP 100, weakness Lightning x2, resistance Fighting
-20, retreat 1.

  Slash      [CC] 30
  Iron Wing  [MMC] 90  Discard a [M] Energy attached to this Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="c2e3275d-15df-585f-823f-8e38cd4a9864",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="HMC",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(title="Slash", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=30),
        Attack(
            title="Iron Wing",
            game_text="Discard a [M] Energy attached to this Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.METAL),
        ),
    ],
)
