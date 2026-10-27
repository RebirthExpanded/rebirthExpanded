"""Mew (MF 11 -- JP MF 011; English 30C/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f1f4b9a6-84ca-5ea1-bbcb-b15b35310858",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=151,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 40, base=10),
        ),
    ],
)
