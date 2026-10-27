"""Aron (SV06 120 -- JP SV6 073; English TWM/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="aa117c8f-f0c3-5593-8cb9-c5e05b2bb038",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=304,
    abilities=[
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=ac.recoil_attack(10),
        ),
    ],
)
