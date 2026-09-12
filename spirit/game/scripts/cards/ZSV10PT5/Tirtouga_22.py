"""Tirtouga (SV - Black Bolt 22/86 -- JP SV11B 025/086, the art here).

Stage 1 Water Pokemon, evolves from Antique Cover Fossil. HP 100, weakness
Lightning x2, no resistance, retreat 3.

  Echoes of Ruin [W] 30x  This attack does 30 damage for each Item card
                          in your opponent's discard pile.
  Surf [WCC] 80

Evolves from the Antique Cover Fossil, not Unidentified Fossil: Pokemon
Research Lab's search does not find it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_discard, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_item_card

card = PokemonCardDef(
    guid="fa9ac61f-c9f7-554f-bd5a-521084750461",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    display_name="Tirtouga",
    searchable_by=["Tirtouga", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueCoverFossil.Name",
    family_id=564,
    abilities=[
        Attack(title="Echoes of Ruin",
               game_text="This attack does 30 damage for each Item card in your opponent's discard pile.",
               cost={PokemonTypes.WATER: 1},
               damage=30, damage_operator="x",
               effect=damage_per(count_discard("opponent", is_item_card), 30)),
        Attack(title="Surf", game_text="",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=80),
    ],
)
