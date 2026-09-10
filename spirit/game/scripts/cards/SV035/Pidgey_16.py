"""Pidgey (SV - 151 016/165).

Basic Colorless Pokemon. HP 50, weakness Lightning x2, resistance
Fighting -30, retreat 1.

  Call for Family [C]     Search your deck for up to 2 Basic Pokemon and
                          put them onto your Bench. Then, shuffle your deck.
  Tackle          [CC] 20

search_to_bench does the whole attack: it caps the two at the Bench space
actually free, takes "up to" as minimum 0, and shuffles afterwards.

The pool's first 151 card, so SV035 is registered here (MEW, sorted
between SV3 and SV4).
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="ba21b6f8-126f-57f7-a439-95de2be8e766",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=16,
    abilities=[
        Attack(
            title="Call for Family",
            game_text=("Search your deck for up to 2 Basic Pokémon and put "
                       "them onto your Bench. Then, shuffle your deck."),
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(
                count=2,
                prompt="Choose up to 2 Basic Pokémon to put onto your Bench.",
            ),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
