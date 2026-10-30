"""Guzma (SM - Burning Shadows 115/147).

  "Switch 1 of your opponent's Benched Pokemon with their Active Pokemon.
   If you do, switch your Active Pokemon with 1 of your Benched Pokemon."

Word for word what Prime Catcher does, so both cards run the same
catcher_switch_both -- the effect moved into card_effects/trainers.py rather
than being spelled out twice. The only differences are the card type
(Supporter, so the once-a-turn Supporter rule applies instead of the ACE SPEC
one) and the set.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import catcher_switch_both, opponent_has_bench

card = SupporterCardDef(
    guid="329d52ad-13e4-5415-8188-eedf45478eca",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=catcher_switch_both,
    condition=opponent_has_bench,
)
