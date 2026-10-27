"""Klang (SV07 100 -- JP SV7 068; English SCR/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="25c6d452-3c84-5c41-a32c-d8576103b3c7",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    display_name="Klang",
    searchable_by=["Klang", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Iron Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.recoil_attack(20),
        ),
    ],
)
