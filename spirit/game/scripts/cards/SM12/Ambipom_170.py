"""Ambipom (SM - Cosmic Eclipse 170/236 -- JP SM12 076/095).

Stage 1 Colorless Pokemon, evolves from Aipom. HP 100, weakness Fighting x2,
retreat 1.

  Nice-Nice Catch  [C]      Draw 2 cards.
  Bye-Bye Throw    [CC] 60x Discard up to 2 cards from your hand. This attack
                            does 60 damage for each card you discarded in
                            this way.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_for_bonus
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="94eb7bed-70c7-5a9d-95a3-56212231c9a2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=['Ambipom', 'Stage 1', 'Ambipom'],
    subtypes=['Stage 1'],
    collector_number=170,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(title="Nice-Nice Catch", game_text="Draw 2 cards.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=draw_attack(2)),
        Attack(title="Bye-Bye Throw", game_text="Discard up to 2 cards from your hand. This attack does 60 damage for each card you discarded in this way.",
               cost={PokemonTypes.COLORLESS: 2}, damage=60, damage_operator="x",
               effect=discard_for_bonus(source="hand", max_count=2, per=60, base=0, prompt="Discard up to 2 cards from your hand")),
    ],
)
