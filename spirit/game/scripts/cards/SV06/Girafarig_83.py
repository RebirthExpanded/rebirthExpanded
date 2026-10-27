"""Girafarig (SV06 83 -- JP SV5a 034; English TWM/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6feb04de-bd46-5261-887d-d820ac9e1132",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=203,
    abilities=[
        Attack(
            title="Dual Headbutt",
            game_text="This attack also does 10 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.snipe_attack(10, pool="bench", side="mine", also_base=True),
        ),
    ],
)
