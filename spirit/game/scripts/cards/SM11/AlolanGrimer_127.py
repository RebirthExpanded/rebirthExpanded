"""Alolan Grimer (SM - Unified Minds 127/236 -- JP SM-M 011/031).

Basic Darkness. HP 80, weakness Fighting x2, resistance Psychic -20,
retreat 2.

  Collect      [C]      Draw 2 cards.
  Sludge Bomb  [CCC] 30

The Darkness printing of Alolan Grimer, alongside the Psychic one from Sun
& Moon that Alolan Muk evolves from. Same name, so either one is a legal
partner for Muk in the client's evolution arrow -- the type does not enter
into it.

Collect draws with no "then" clause, so the empty-deck gate is the only
thing standing between it and an empty deck; draw_cards takes what is
there.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="d14fe3a1-d883-56d2-ace6-d68ae21192e0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    display_name="Alolan Grimer",
    searchable_by=["Alolan Grimer", "Basic", "AlolanGrimer"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=88,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
