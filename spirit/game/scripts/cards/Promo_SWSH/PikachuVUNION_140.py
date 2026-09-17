"""Pikachu V-UNION, top-right piece (SWSH Promo 140 -- JP S8a 026/028, the art
here).

One of the four Pokemon V-UNION cards. This piece prints Shocking Shock [LC] 120;
the Pokemon that stands on the board is PikachuVUNION_143 (HP 300, all
four attacks, 3 Prizes). A piece is a Pokemon card -- a Pokemon V with a
rule box -- that can't be played from hand and never stands alone: the
four combine from the discard pile, once per game, through the rule
offered on each piece there (not an Ability: no lock reaches it).
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import vunion_assembly_ability
from spirit.game.data_utils import VUnionPieceCardDef, sibling_card

_UNION = sibling_card(__file__, "PikachuVUNION_143.py")

card = VUnionPieceCardDef(
    vunion="Promo_SWSH/PikachuVUNION_143",
    position="top-right",
    guid="daa87b6a-74eb-53fd-8ea1-2e08b7024be6",
    key="Promo_SWSH",
    name=_UNION.name,
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    subtypes=["V-UNION"],
    collector_number=140,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        vunion_assembly_ability("Pikachu V-UNION"),
        _UNION.abilities[1],
    ],
)
