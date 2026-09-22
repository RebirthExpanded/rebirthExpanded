"""Magikarp (XY - Ancient Origins 19/98 -- JP XY7 019/081, the art here).

Basic Water Pokemon. HP 30, weakness Lightning x2, retreat 1.

  Epic Splash  [W] 30  Flip 2 coins. If either of them is tails, this
                       attack does nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="b00ffb84-b13d-5f93-b7ba-fcca0ae27c25",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Epic Splash",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=flip_or_nothing(coins=2),
        ),
    ],
)
