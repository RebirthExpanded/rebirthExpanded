"""Darkrai & Cresselia LEGEND, bottom half (HS - Triumphant 100/102 -- JP 30th
CELEBRATION M6a 152/103, the art here).

One of the two LEGEND cards. Played together from your hand with the
top half, the two become DarkraiCresseliaLEGEND_901 (HP 150, Darkness /
Psychic, Lost Crisis and Moon's Invite, 2 Prizes). On its own it is a
Pokemon card in the hand (searchable as one) that can't be played.

Legacy / Unlimited only: HGSS4 is not an Expanded set in this pool.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import LegendHalf, LegendHalfCardDef

card = LegendHalfCardDef(
    legend="HGSS4/DarkraiCresseliaLEGEND_901",
    half=LegendHalf.BOTTOM,
    guid="051a608b-4262-5fc2-91da-8ba512b1d7a2",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiCresseliaLEGEND.Name",
    display_name="Darkrai & Cresselia LEGEND",
    searchable_by=["Darkrai & Cresselia LEGEND", "LEGEND", "DarkraiCresseliaLEGEND"],
    subtypes=["LEGEND"],
    collector_number=100,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.PSYCHIC],
)
