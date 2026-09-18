"""Zacian V-UNION, top-left piece (SWSH Promo 163 -- JP Special Card Set
009/013, the art here).

One of the four Pokemon V-UNION cards. This piece prints Union Gain [C];
the Pokemon that stands on the board is ZacianVUNION_903 (HP 320, everything
the four print, 3 Prizes). A piece is a Pokemon card -- a Pokemon V with a
rule box -- that can't be played from hand and never stands alone: the four
combine from the discard pile, once per game, through the rule offered on
each piece there (not an Ability: no lock reaches it).
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import vunion_assembly_ability
from spirit.game.data_utils import VUnionPieceCardDef, sibling_card

_UNION = sibling_card(__file__, "ZacianVUNION_903.py")

card = VUnionPieceCardDef(
    vunion="Promo_SWSH/ZacianVUNION_903",
    position="top-left",
    guid="d739d78b-7318-56e1-aa63-9a878b0142be",
    key="Promo_SWSH",
    name=_UNION.name,
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    subtypes=["V-UNION"],
    collector_number=163,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=320,
    elements=[PokemonTypes.METAL],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        vunion_assembly_ability("Zacian V-UNION"),
        _UNION.abilities[0],
    ],
)
