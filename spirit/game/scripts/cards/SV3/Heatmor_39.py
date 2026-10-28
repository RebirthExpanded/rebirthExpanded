"""Heatmor (SV3 39 -- JP SV3 019; English OBF/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9be52cf4-61aa-5784-a400-c4cc54d9a450",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Energy Burner",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 30, base=30),
        ),
    ],
)
