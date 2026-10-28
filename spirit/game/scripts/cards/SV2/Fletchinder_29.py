"""Fletchinder (SV2 29 -- JP SV2D 012; English PAL/199, PAL/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5d0e4599-c529-5aa1-903f-e4b6a9ba282e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    display_name="Fletchinder",
    searchable_by=["Fletchinder", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Heat Dive",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=ac.recoil_attack(10),
        ),
    ],
)
