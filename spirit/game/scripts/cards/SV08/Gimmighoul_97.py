"""Gimmighoul (SV - Surging Sparks 97/191 -- JP SV7a 024/064).

Basic Psychic Pokemon. HP 70, weakness Darkness x2, resistance Fighting
-30, retreat 2.

  Minor Errand-Running  [C]  Search your deck for up to 2 Basic Energy
                             cards, reveal them, and put them into your
                             hand. Then, shuffle your deck.
  Tackle  [CCC] 50
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_energy

card = PokemonCardDef(
    guid="df326f55-c759-5962-a565-c31924ee9ca3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV08",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=999,
    regulation_mark="H",
    abilities=[
        Attack(title="Minor Errand-Running",
               game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=search_to_hand(is_basic_energy, count=2, reveal=True)),
        Attack(title="Tackle", game_text="", cost={PokemonTypes.COLORLESS: 3}, damage=50),
    ],
)
