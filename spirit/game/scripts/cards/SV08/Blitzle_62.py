"""Blitzle (SV - Surging Sparks 62/191 -- JP SV8 038/106).

Basic Lightning Pokemon. HP 70, weakness Fighting x2, retreat 1.

  Add On        [C]     Draw a card.
  Static Shock  [LC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="9c96f4a7-37b0-518c-bc8a-61b57b6a847a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV08",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=522,
    regulation_mark="H",
    abilities=[
        Attack(title="Add On", game_text="Draw a card.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0, effect=draw_attack(1)),
        Attack(title="Static Shock", game_text="",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20),
    ],
)
