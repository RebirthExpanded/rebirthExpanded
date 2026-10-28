"""Naclstack (SV4 103 -- JP SV4K 039; English PAR/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4de7f7b5-5d19-56b7-99db-58b204ad0cca",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    display_name="Naclstack",
    searchable_by=["Naclstack", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    family_id=932,
    abilities=[
        Attack(
            title="Rocky Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=ac.recoil_attack(30),
        ),
    ],
)
