"""Gloom (ME2 2 -- JP M2 002; English PFL/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7e487eed-0417-57c7-bea2-5efe6f0d6392",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Disperse Drool",
            game_text="This attack also does 20 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=ac.spread_damage(20, side="both", also_base=True),
        ),
    ],
)
