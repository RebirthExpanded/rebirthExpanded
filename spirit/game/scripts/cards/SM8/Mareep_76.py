"""Mareep (SM - Lost Thunder 76/214 -- JP SM8 034/095).

Basic Lightning Pokemon. HP 60, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Thunder Shock  [L] 10  Flip a coin. If heads, your opponent's Active
                         Pokemon is now Paralyzed.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="2cae4bf0-2fb5-591c-b42e-cca183ea78fb",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    display_name="Mareep",
    searchable_by=['Mareep', 'Basic', 'Mareep'],
    subtypes=['Basic'],
    collector_number=76,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=179,
    abilities=[
        Attack(title="Thunder Shock", game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
               cost={PokemonTypes.LIGHTNING: 1}, damage=10,
               effect=condition_attack(SpecialConditions.PARALYZED, flip=True)),
    ],
)
