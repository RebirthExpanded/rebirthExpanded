"""Alolan Meowth (SM Black Star Promos SM51 -- JP SM-P 032).

Basic Darkness. HP 60, weakness Fighting x2, resistance Psychic -20,
retreat 1.

  Nasty Plot  [C]     Flip a coin. If heads, search your deck for a card
                      and put it into your hand. Then, shuffle your deck.
  Scratch     [D] 10

The coin decides before the deck opens, so a tails costs the attack and
nothing else. With an empty deck the search finds nothing -- an attack can
always be declared, which is why there is no gate here where a Trainer
would have one.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="cd5e7fb3-6f2a-52dd-b754-fd61529fb732",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    display_name="Alolan Meowth",
    searchable_by=["Alolan Meowth", "Basic", "AlolanMeowth"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_or_nothing(then=search_to_hand(
                count=1, minimum=0,
                prompt="Choose a card to put into your hand.")),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
