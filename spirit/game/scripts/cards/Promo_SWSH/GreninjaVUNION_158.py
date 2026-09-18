"""Greninja V-UNION, bottom-right piece (SWSH Promo 158 -- JP Special Card Set
004/013, the art here).

One of the four Pokemon V-UNION cards. This piece prints Feel the Way and Waterfall Bind [WWC] 180;
the Pokemon that stands on the board is GreninjaVUNION_901 (HP 300, everything
the four print, 3 Prizes). A piece is a Pokemon card -- a Pokemon V with a
rule box -- that can't be played from hand and never stands alone: the four
combine from the discard pile, once per game, through the rule offered on
each piece there (not an Ability: no lock reaches it).
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import vunion_assembly_ability
from spirit.game.data_utils import VUnionPieceCardDef, sibling_card

_UNION = sibling_card(__file__, "GreninjaVUNION_901.py")

card = VUnionPieceCardDef(
    vunion="Promo_SWSH/GreninjaVUNION_901",
    position="bottom-right",
    guid="ff95fbdf-2e57-587c-9d97-3726ffdac288",
    key="Promo_SWSH",
    name=_UNION.name,
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    subtypes=["V-UNION"],
    collector_number=158,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=300,
    elements=[PokemonTypes.WATER],
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=658,
    abilities=[
        vunion_assembly_ability("Greninja V-UNION"),
        _UNION.abilities[5],
        _UNION.abilities[6],
    ],
)
