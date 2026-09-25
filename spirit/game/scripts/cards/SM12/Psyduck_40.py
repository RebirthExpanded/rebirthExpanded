"""Psyduck (SM - Cosmic Eclipse 40/236 -- JP SM11a 017/064).

Basic Water Pokemon. HP 60, weakness Grass x2, retreat 1.

  Scratch         [C] 10
  Confusion Wave  [WC] 20  Both Active Pokemon are now Confused.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="2400edcb-c22f-5cbf-92d9-be2556d77270",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=['Psyduck', 'Basic', 'Psyduck'],
    subtypes=['Basic'],
    collector_number=40,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(title="Scratch", game_text="",
               cost={PokemonTypes.COLORLESS: 1}, damage=10),
        Attack(title="Confusion Wave", game_text="Both Active Pokémon are now Confused.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20,
               effect=condition_attack(SpecialConditions.CONFUSED, both_actives=True)),
    ],
)
