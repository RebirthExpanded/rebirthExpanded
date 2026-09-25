"""Type: Null (SM - Unified Minds 183/236 -- JP SM10b 042/054).

Basic Colorless Pokemon. HP 100, weakness Fighting x2, retreat 1.

  Smash Kick  [C] 20
  Quick Blow  [CC] 30+  Flip a coin. If heads, this attack does 30 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="c5778967-b1b5-5e96-ac36-a4fe4d557443",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    display_name="Type: Null",
    searchable_by=['Type: Null', 'Basic', 'TypeNull'],
    subtypes=['Basic'],
    collector_number=183,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=772,
    abilities=[
        Attack(title="Smash Kick", game_text="",
               cost={PokemonTypes.COLORLESS: 1}, damage=20),
        Attack(title="Quick Blow", game_text="Flip a coin. If heads, this attack does 30 more damage.",
               cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator="+",
               effect=flip_bonus(30)),
    ],
)
