"""Darumaka (SV06 34 -- JP SV6 017; English TWM/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="77019ab9-5073-50d7-9bb2-e96cf76c3331",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Fire Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=ac.recoil_attack(20),
        ),
    ],
)
