"""Tympole (SM - Cosmic Eclipse 58/236 -- JP SM11b 012/049).

Basic Water Pokemon. HP 60, weakness Grass x2, retreat 1.

  Flail Around  [C] 10x  Flip 3 coins. This attack does 10 damage for each
                         heads.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="ace542d9-0c4d-5d76-a029-4811cba112e8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=['Tympole', 'Basic', 'Tympole'],
    subtypes=['Basic'],
    collector_number=58,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=535,
    abilities=[
        Attack(title="Flail Around", game_text="Flip 3 coins. This attack does 10 damage for each heads.",
               cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator="x",
               effect=flip_damage(coins=3, per_heads=10)),
    ],
)
