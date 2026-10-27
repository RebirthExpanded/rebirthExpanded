"""Tapu Bulu (SV065 6 -- JP SV6a 006; English SFA/6, SFA/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ac87e347-0c17-5559-b195-93987bf4fc75",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name",
    display_name="Tapu Bulu",
    searchable_by=["Tapu Bulu", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=787,
    abilities=[
        Attack(
            title="Wood Hammer",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=ac.recoil_attack(30),
        ),
    ],
)
