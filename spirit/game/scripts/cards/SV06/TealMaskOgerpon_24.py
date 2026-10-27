"""Teal Mask Ogerpon (SV06 24 -- JP SV6 015; English SVP/123, TWM/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="88d0b2ef-7ee3-5729-a819-fed9a0210a94",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerpon.Name",
    display_name="Teal Mask Ogerpon",
    searchable_by=["Teal Mask Ogerpon", "Basic"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1017,
    abilities=[
        Attack(
            title="Mountain Stroll",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
        Attack(
            title="Ogre Comeback",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("opponent"), 20, base=20),
        ),
    ],
)
