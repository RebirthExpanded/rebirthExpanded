"""Darkrai & Cresselia LEGEND, top half (HS - Triumphant 99/102 -- JP 30th
CELEBRATION M6a 151/103, the art here).

One of the two LEGEND cards. Played together from your hand with the
bottom half, the two become DarkraiCresseliaLEGEND_901 (HP 150, Darkness /
Psychic, Lost Crisis and Moon's Invite, 2 Prizes). On its own it is a
Pokemon card in the hand (searchable as one) that can't be played.

Legacy / Unlimited only: HGSS4 is not an Expanded set in this pool.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import LegendHalf, LegendHalfCardDef

card = LegendHalfCardDef(
    legend="HGSS4/DarkraiCresseliaLEGEND_901",
    half=LegendHalf.TOP,
    guid="742561ac-1b36-5577-9eb4-ed1957ca953a",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiCresseliaLEGEND.Name",
    display_name="Darkrai & Cresselia LEGEND",
    searchable_by=["Darkrai & Cresselia LEGEND", "LEGEND", "DarkraiCresseliaLEGEND"],
    subtypes=["LEGEND"],
    collector_number=99,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.PSYCHIC],
)
