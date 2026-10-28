"""Blitzle (SV4 62 -- JP SV4M 023; English PAR/195, PAR/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d6ced380-f54e-50ec-9b91-d483e26a4ad1",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=522,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Wild Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.recoil_attack(20),
        ),
    ],
)
