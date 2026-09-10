"""Lillipup (BW - Black & White 80/114).

Basic Colorless Pokemon. HP 50, weakness Fighting x2, no resistance,
retreat 1.

  Pickup [C]     Put an Item card from your discard pile into your hand.
  Bite   [C] 10

"An Item card" is asked through data_utils.counts_as_item, which no
Pokemon Tool answers: Tools are their own category now, whatever their own
type line says, so Float Stone is not on offer here. The pick is mandatory
once there is something to take, and there is simply nothing to do with an
Item-less discard pile.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, counts_as_item
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard

card = PokemonCardDef(
    guid="38fcd5d6-19cf-552d-a59b-60b273f45a8b",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic", "Lillipup"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Pickup",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                lambda c: counts_as_item(c.archetype_id),
                count=1, minimum=1, reveal=False, to="hand",
                prompt="Choose an Item card to put into your hand.",
            ),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
