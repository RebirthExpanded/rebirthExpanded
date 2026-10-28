"""Luvdisc (SV2 47 -- JP SV2P 018; English PAL/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="290a63cd-104a-505e-89c5-2541121cde4c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Matching",
            game_text="Search your deck for up to 2 Supporter cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_supporter_card, count=2, reveal=True, prompt="Choose up to 2 Supporter cards."),
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
