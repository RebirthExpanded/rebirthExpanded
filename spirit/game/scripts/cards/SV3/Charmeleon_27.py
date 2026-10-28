"""Charmeleon (SV3 27 -- JP SV3 013; English OBF/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="523baae7-e383-59f5-9c61-a93f13d86394",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 2},
            damage=70,
            effect=ac.recoil_attack(20),
        ),
    ],
)
