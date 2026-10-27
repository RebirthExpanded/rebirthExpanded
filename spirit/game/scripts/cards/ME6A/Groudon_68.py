"""Groudon (ME6A 68 -- JP M6a 068; English 30C/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="69689dcb-b39d-5f6b-bf59-0dd1394391f0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Break Ground",
            game_text="This attack also does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 5},
            damage=250,
            effect=ac.spread_damage(20, side="mine", also_base=True),
        ),
    ],
)
