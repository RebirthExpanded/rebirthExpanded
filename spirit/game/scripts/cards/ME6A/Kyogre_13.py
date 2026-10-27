"""Kyogre (ME6A 13 -- JP M6a 013; English 30C/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a8f6df6a-6c98-55fc-9ab6-260307a1afed",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Hydro Pump",
            game_text="This attack does 30 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", PokemonTypes.WATER), 30, base=60),
        ),
    ],
)
