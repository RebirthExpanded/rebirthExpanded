"""Morpeko V-UNION, top-right piece (SWSH Promo 216 -- JP VMAX Climax
057/184, the art here).

One of the four Pokemon V-UNION cards. This piece prints All You Can Eat [CC];
the Pokemon that stands on the board is MorpekoVUNION_905 (HP 310, everything
the four print, 3 Prizes). A piece is a Pokemon card -- a Pokemon V with a
rule box -- that can't be played from hand and never stands alone: the four
combine from the discard pile, once per game, through the rule offered on
each piece there (not an Ability: no lock reaches it).
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import vunion_assembly_ability
from spirit.game.data_utils import VUnionPieceCardDef, sibling_card

_UNION = sibling_card(__file__, "MorpekoVUNION_905.py")

card = VUnionPieceCardDef(
    vunion="Promo_SWSH/MorpekoVUNION_905",
    position="top-right",
    guid="3e01c327-ad77-5ee2-a841-ad40103887d4",
    key="Promo_SWSH",
    name=_UNION.name,
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    subtypes=["V-UNION"],
    collector_number=216,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        vunion_assembly_ability("Morpeko V-UNION"),
        _UNION.abilities[1],
    ],
)
