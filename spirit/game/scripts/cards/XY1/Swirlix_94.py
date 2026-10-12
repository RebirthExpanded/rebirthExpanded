"""Swirlix (XY 94/146 -- JP XY1-Bx 042/060, the art here).

Basic Fairy Pokemon. HP 60, weakness Metal x2, resistance Darkness -20,
retreat 1.

  Tackle      [C]   10
  Fairy Wind  [YC]  20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    # GUID kept from when this card was filed as XY1 95: renumbering it
    # must not break saved decks (and SM8-14 is taken by the old Skiploom).
    guid="7bb6e0a7-c4f4-5a2b-9086-55e1b69fc9a3",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    display_name="Swirlix",
    searchable_by=["Swirlix", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=684,
    abilities=[
        Attack(title="Tackle", game_text="", cost={PokemonTypes.COLORLESS: 1}, damage=10),
        Attack(title="Fairy Wind", game_text="",
               cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1}, damage=20),
    ],
)
