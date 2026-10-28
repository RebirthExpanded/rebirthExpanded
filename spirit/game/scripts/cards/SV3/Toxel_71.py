"""Toxel (SV3 71 -- JP SV3 037; English OBF/71, PAF/140, SVP/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="416ec3f2-3fe6-5330-9220-5bd3f665ab21",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    display_name="Toxel",
    searchable_by=["Toxel", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=848,
    abilities=[
        Attack(
            title="Slight Intrusion",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
