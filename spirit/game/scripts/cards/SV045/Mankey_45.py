"""Mankey (SV045 45 -- JP SV1V 049; English PAF/169, PAF/45, SVI/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e8bdb7b6-f2f1-5011-a21b-c364c6dbdc12",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Monkey Beatdown",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
