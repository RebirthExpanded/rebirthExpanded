"""Charmeleon (JP CP3 "Pokekyun Collection" 004/032 -- no English print of
this text; pool slot Promo_XY 903).

Stage 1 Fire Pokemon, evolves from Charmander. HP 90, weakness Water x2,
retreat 2.

  Friend Call  [C]  Search your deck for a Supporter card, reveal it, and
                    put it into your hand. Then, shuffle your deck.
  Slash  [RRC] 80
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_supporter_card

card = PokemonCardDef(
    guid="56d68d23-6992-5edf-8d59-c896b3f16916",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=903,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(title="Friend Call",
               game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=search_to_hand(is_supporter_card, count=1, reveal=True)),
        Attack(title="Slash", game_text="",
               cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=80),
    ],
)
