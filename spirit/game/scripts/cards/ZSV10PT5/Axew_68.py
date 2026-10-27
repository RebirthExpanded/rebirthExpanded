"""Axew (ZSV10PT5 68 -- JP SV11B 070; English BLK/145, BLK/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="33c2bc23-e2cd-5382-a46b-dd07374b8ed9",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=610,
    abilities=[
        Attack(
            title="Gather Strength",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
    ],
)
