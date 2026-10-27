"""Musharna (ZSV10PT5 36 -- JP SV11B 039; English BLK/117, BLK/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for


def _fennel(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Fennel"


card = PokemonCardDef(
    guid="1f196dcd-4100-5f2a-a76c-f3a9fb7ec158",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Attack(
            title="Dream Calling",
            game_text="You may search your deck for any number of Fennel cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(_fennel, count=60, reveal=True, prompt="Choose any number of Fennel cards."),
        ),
        Attack(
            title="Sleep Pulse",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
