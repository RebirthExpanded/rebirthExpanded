"""Steelix (SV4 125 -- JP SV4M 041; English PAR/125, PAR/208). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="028e8d07-0773-53b4-a70f-dbb270c2f992",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=125,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="This attack also does 30 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 1},
            damage=130,
            effect=ac.spread_damage(30, side="mine", also_base=True),
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 3},
            damage=180,
        ),
    ],
)
