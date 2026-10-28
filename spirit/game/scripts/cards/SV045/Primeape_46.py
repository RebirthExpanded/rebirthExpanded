"""Primeape (SV045 46 -- JP SV1V 050; English PAF/170, PAF/46, SVI/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="360f4ef8-d3b6-543d-a5fb-008164c1c928",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Raging Punch",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            effect=ac.recoil_attack(20),
        ),
    ],
)
