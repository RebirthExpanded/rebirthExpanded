"""Mewtwo V-UNION, top-left piece (SWSH Promo 159 -- JP Special Card Set
005/013, the art here).

One of the four Pokemon V-UNION cards. This piece prints Union Gain [C];
the Pokemon that stands on the board is MewtwoVUNION_902 (HP 310, everything
the four print, 3 Prizes). A piece is a Pokemon card -- a Pokemon V with a
rule box -- that can't be played from hand and never stands alone: the four
combine from the discard pile, once per game, through the rule offered on
each piece there (not an Ability: no lock reaches it).
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import vunion_assembly_ability
from spirit.game.data_utils import VUnionPieceCardDef, sibling_card

_UNION = sibling_card(__file__, "MewtwoVUNION_902.py")

card = VUnionPieceCardDef(
    vunion="Promo_SWSH/MewtwoVUNION_902",
    position="top-left",
    guid="1ade5e66-8def-5dd7-a3c6-d0d6ad5c2d2c",
    key="Promo_SWSH",
    name=_UNION.name,
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    subtypes=["V-UNION"],
    collector_number=159,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        vunion_assembly_ability("Mewtwo V-UNION"),
        _UNION.abilities[0],
    ],
)
