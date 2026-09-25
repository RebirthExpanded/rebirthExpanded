"""Passimian (SM - Cosmic Eclipse 125/236 -- JP SM11a 037/064).

Basic Fighting Pokemon. HP 110, weakness Psychic x2, retreat 1.

  Spike Draw     [F] 20    Draw 2 cards.
  Seismic Toss   [FCC] 70
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="3b4a29fd-d44d-5d42-ab75-1a975951dee5",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=['Passimian', 'Basic', 'Passimian'],
    subtypes=['Basic'],
    collector_number=125,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(title="Spike Draw", game_text="Draw 2 cards.",
               cost={PokemonTypes.FIGHTING: 1}, damage=20,
               effect=draw_attack(2)),
        Attack(title="Seismic Toss", game_text="",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=70),
    ],
)
