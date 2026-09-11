"""Jirachi-EX (BW - Plasma Blast 60/101 -- JP BW9-B 048/070).

Basic Metal Pokemon-EX. HP 90, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Ability  Stellar Guidance  When you play this Pokemon from your hand onto
                             your Bench, you may search your deck for a
                             Supporter card, reveal it, and put it into your
                             hand. Shuffle your deck afterward.
  Hypnostrike  [MCC] 60  Both this Pokemon and the Defending Pokemon are now
                         Asleep.

"When you play this Pokemon from your hand onto your Bench" is the ON_PLAY
window, which only the hand-to-Bench play opens: a Jirachi-EX that reaches
the Bench any other way (Ultra Ball's target is the hand, but Nest Ball puts
it there from the DECK) does not fire it.

An uppercase Pokemon-EX, so it is worth 2 Prizes and answers to every card
in the pool that reads "Pokemon-EX".
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef, Triggers)
from spirit.game.session.effects import is_supporter_card

card = PokemonCardDef(
    guid="d462a591-e296-5093-b3ba-39c7d18aed22",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiEX.Name",
    display_name="Jirachi-EX",
    searchable_by=["Jirachi-EX", "Basic", "EX", "JirachiEX"],
    subtypes=["Basic", "EX"],
    collector_number=60,
    set_code="BW10",
    rarity=Rarities.RareUltra,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Guidance",
            game_text="When you play this Pokémon from your hand onto your Bench, you may search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(
                is_supporter_card, count=1, minimum=0, reveal=True,
                prompt="Choose a Supporter card to put into your hand."),
        ),
        Attack(
            title="Hypnostrike",
            game_text="Both this Pokémon and the Defending Pokémon are now Asleep.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP,
                                    both_actives=True),
        ),
    ],
)
